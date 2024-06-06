from django.contrib import admin
# local imports
from apps.vendor.models import Vendor, HistoricalPerformance


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    """
    admin interface for Vendor.
    """
    list_display = ('id', 'name')


@admin.register(HistoricalPerformance)
class PerformanceMetricsAdmin(admin.ModelAdmin):
    """
    admin interface for performance.
    """
    list_display = ('id', 'vendor', 'on_time_delivery_rate')
