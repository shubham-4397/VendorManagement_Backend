"""
signals file
"""
from django.db.models import Avg, F, ExpressionWrapper, DurationField
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.vendor.models import HistoricalPerformance, Vendor
from apps.orders.models import PurchaseOrder
from apps.orders.choices import OrderStatus


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_metrics(sender, instance, created, **kwargs):
    """signal to update performance of the vendor"""
    total_orders = PurchaseOrder.objects.filter(vendor=instance.vendor)
    completed_orders = total_orders.filter(status=OrderStatus.COMPLETED.value)
    # avg_response_time
    avg_resp_time = total_orders.aggregate(avg_time=Avg(ExpressionWrapper(F('issue_date') - F('acknowledgment_date'),
                                                                          output_field=DurationField())))['avg_time']
    # fulfillment_rate
    fulfillment_rate = completed_orders.count() / total_orders.count() if total_orders.count() > 0 else 0
    qs = HistoricalPerformance.objects.filter(vendor=instance.vendor)
    on_time_delivery = 0
    quality_rating_avg = 0
    if instance.status == OrderStatus.COMPLETED.value:
        # quality_rating_avg
        quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg']
        # on_time_delivery_rate
        if instance.delivery_date:
            total_orders_on_time = total_orders.filter(delivery_date__lte=instance.delivery_date).count()
            on_time_delivery = total_orders_on_time / completed_orders.count() if completed_orders.count() > 0 else 0
    performance_metrics = {
        'on_time_delivery_rate': on_time_delivery,
        'quality_rating_avg': quality_rating_avg,
        'average_response_time': avg_resp_time.total_seconds() if avg_resp_time else 0,
        'fulfillment_rate': fulfillment_rate
    }
    if qs.first():
        qs.update(**performance_metrics)
    else:
        HistoricalPerformance.objects.create(vendor=instance.vendor, **performance_metrics)
