"""
utility urls file
"""
# third party imports
from rest_framework import routers

from apps.orders.views import PurchaseOrderViewSet

# local imports

router = routers.SimpleRouter()

router.register('purchase_orders', PurchaseOrderViewSet, 'purchase_orders')

urlpatterns = [

] + router.urls
