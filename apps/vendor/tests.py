from django.urls import reverse
from rest_framework.test import APITestCase
from apps.vendor.models import Vendor


class VendorTestCases(APITestCase):
    """
    Basic setup
    """

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
        self.vendor_url = reverse("api:vendor-list")
        self.vendor_url_id = reverse("api:vendor-detail", kwargs={'pk': self.vendor.id})
        self.vendor_url_id_not_found = reverse("api:vendor-detail", kwargs={'pk': 10})
        self.performance_url = reverse("api:vendor-performance", kwargs={'pk': self.vendor.id})

        self.vendor_create = {
            'name': 'abc',
            'contact_details': '9876543210',
            'address': 'axz',
            'vendor_code': 'abc123'
        }
        self.vendor_code = {
            'name': 'abc',
            'contact_details': '9876543210',
            'address': 'axz',
            'vendor_code': 'xyz123'
        }

    def test_vendor_list_with_valid_data(self):
        """
        Test the get method with valid data
        """
        response = self.client.get(f"{self.vendor_url}", format="json")
        self.assertEqual(response.status_code, 200)

    def test_vendor_post_with_valid_data(self):
        response = self.client.post(f"{self.vendor_url}", self.vendor_create, format="json")
        self.assertEqual(response.status_code, 200)

    def test_vendor_post_with_non_unique_vendor_code(self):
        response = self.client.post(f"{self.vendor_url}", self.vendor_code, format="json")
        self.assertEqual(response.status_code, 400)

    def test_vendor_get_with_id(self):
        response = self.client.get(f"{self.vendor_url_id}", format="json")
        self.assertEqual(response.status_code, 200)

    def test_vendor_get_with_id_not_found(self):
        response = self.client.get(f"{self.vendor_url_id_not_found}", format="json")
        self.assertEqual(response.status_code, 404)

    def test_vendor_update_with_id_not_found(self):
        response = self.client.put(f"{self.vendor_url_id_not_found}", format="json")
        self.assertEqual(response.status_code, 404)

    def test_vendor_update_with_id(self):
        response = self.client.put(f"{self.vendor_url_id}", self.vendor_create, format="json")
        self.assertEqual(response.status_code, 200)

    def test_delete_vendor_with_id(self):
        response = self.client.delete(f"{self.vendor_url_id}", format="json")
        self.assertEqual(response.status_code, 200)
