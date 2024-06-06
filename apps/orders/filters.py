from django.db.models import Q
from django_filters import rest_framework as filters


class PurchaseOrderFilters(filters.FilterSet):
    """
    Filter by vendor id.
    """
    vendor_id = filters.CharFilter()

    def filter_queryset(self, queryset):
        vendor_id = self.data.get('vendor_id')
        vendor_query = Q()
        if vendor_id:
            vendor_query &= Q(vendor=vendor_id)
        return queryset.filter(vendor_query)

