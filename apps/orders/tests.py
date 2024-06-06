from django.urls import reverse
from rest_framework.test import APITestCase
from apps.orders.models import PurchaseOrder
from apps.vendor.models import Vendor


class PurchaseOrderTestCases(APITestCase):
    """Basic setup"""

    def setUp(self):
        """
        vendor setup
        """
        self.vendor = Vendor.objects.create(
            name="xyz",
            contact_details="987654321",
            address="abc",
            vendor_code="xyz123",
        )
        self.vendor.save()
        self.po = PurchaseOrder.objects.create(
            po_number="xyz",
            vendor=self.vendor,

        )
        self.po.save()
        self.po_get_url = reverse("order_api:purchase_orders-list")
        self.po_get_url_id = reverse("order_api:purchase_orders-detail", kwargs={'pk': self.po.id})
        self.po_get_url_filter = reverse("order_api:purchase_orders-list")
        self.vendor_filter = {
            'vendor_id': self.vendor.id
        }
        self.po_create = {
            'po_number': 'book1',
            'vendor': self.vendor.id,
            'items': {},
            'quantity': 1
        }

    def test_po_list_with_valid_data(self):
        """Test the get method with valid data"""
        response = self.client.get(f"{self.po_get_url}", format="json")
        self.assertEqual(response.status_code, 200)

    def test_filter_po_list_with_vendor_id(self):
        """Test the get method with filter by vendor"""
        response = self.client.get(f"{self.po_get_url}", self.vendor_filter, format="json")
        self.assertEqual(response.status_code, 200)

    def test_po_post_method_with_valid_data(self):
        """Test purchase order create method"""
        response = self.client.post(f"{self.po_get_url}", self.po_create, format="json")
        self.assertEqual(response.status_code, 200)

    def test_po_get_with_id(self):
        """retrieve the po with id"""
        response = self.client.get(f"{self.po_get_url_id}", format="json")
        self.assertEqual(response.status_code, 200)

    def test_delete_vendor_with_id(self):
        """delete the purchase order"""
        response = self.client.delete(f"{self.po_get_url_id}", format="json")
        self.assertEqual(response.status_code, 200)
