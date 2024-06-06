from django.db import models
from apps.vendor.models import Vendor
from apps.orders.choices import OrderStatus


class PurchaseOrder(models.Model):
    """
    purchase model to store all the details of the orders
    """
    po_number = models.CharField(unique=True, max_length=50)
    vendor = models.ForeignKey(Vendor, related_name='vendor', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    items = models.JSONField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default=OrderStatus.PENDING.value,
                              help_text='can be pending, completed, cancelled')
    quality_rating = models.FloatField(default=0.0)
    issue_date = models.DateTimeField(blank=True, null=True)
    acknowledgment_date = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()

    def __str__(self) -> str:
        """ string representation """
        return f"{self.vendor}"


