"""
Vendor Model
"""

from django.db import models


class Vendor(models.Model):
    """
    Vendor model to store all the details of the vendor
    """
    name = models.CharField(max_length=50, blank=True, null=True)
    contact_details = models.TextField(max_length=100, blank=True, null=True)
    address = models.TextField(max_length=100, null=True, blank=True)
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)

    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    objects = models.Manager()

    def __str__(self) -> str:
        """ string representation """
        return f"{self.name}"


class HistoricalPerformance(models.Model):
    """
    used to store the performance of the vendor
    """
    vendor = models.ForeignKey(Vendor, related_name='vendor_performance', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    objects = models.Manager()

    def __str__(self) -> str:
        """ string representation """
        return f"{self.vendor}"
