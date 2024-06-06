"""
Vendor Serializer
"""
from rest_framework import serializers

from apps.vendor.messages import ERROR_MESSAGE
from apps.vendor.models import Vendor, HistoricalPerformance


class VendorListSerializer(serializers.ModelSerializer):
    """
    used to list all the vendors
    """
    class Meta:
        model = Vendor
        fields = "__all__"


class VendorSerializer(serializers.ModelSerializer):
    """
    used to serialize the vendor objects
    """

    class Meta:
        """
        meta class
        """
        model = Vendor
        fields = ('name', 'contact_details', 'address', 'vendor_code')

    def validate(self, attrs):
        """ used to validate the data """
        name = attrs.get('name')
        if not name:
            raise serializers.ValidationError(ERROR_MESSAGE['name_incorrect'])
        return attrs

    def create(self, validated_data):
        """used to create the vendor"""
        return super(VendorSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        """used to update the vendor details"""
        return super(VendorSerializer, self).update(instance=instance, validated_data=validated_data)


class VendorPerformanceSerializer(serializers.ModelSerializer):
    """vendor performance serializer"""

    class Meta:
        model = HistoricalPerformance
        fields = ('on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')

