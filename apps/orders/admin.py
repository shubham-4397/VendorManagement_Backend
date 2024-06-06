from django.contrib import admin
# local imports
from apps.orders.models import PurchaseOrder


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    """
    admin interface for Orders.
    """
    list_display = ('id', 'vendor', 'po_number', 'quality_rating', 'status')
