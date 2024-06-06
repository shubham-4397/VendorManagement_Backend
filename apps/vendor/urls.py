"""
utility urls file
"""
# third party imports
from rest_framework import routers

from apps.vendor.views import VendorViewSet

# local imports

router = routers.SimpleRouter()

router.register('vendor', VendorViewSet, 'vendor')

urlpatterns = [

] + router.urls
