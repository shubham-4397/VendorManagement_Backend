"""
Purchase Order Serializer
"""
from django.utils import timezone
from rest_framework import serializers

from apps.orders.messages import ERROR_MESSAGE
from apps.orders.models import PurchaseOrder


class PurchaseOrderListSerializer(serializers.ModelSerializer):
    """
    used to list all the Orders
    """
    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class UpdateAcknowledgeSerializer(serializers.ModelSerializer):
    """
    used to update acknowledgement of po by the vendor
    """
    class Meta:
        model = PurchaseOrder
        fields = ('acknowledgment_date', )

    def validate(self, attrs):
        """validate the acknowledgment_date"""
        ack_date = attrs.get("acknowledgment_date")
        if ack_date > timezone.now():
            raise serializers.ValidationError(ERROR_MESSAGE['future_date'])
        return attrs

    def create(self, validated_data):
        """create the instance"""
        return super(UpdateAcknowledgeSerializer, self).create(validated_data)


class PurchaseOrderSerializer(serializers.ModelSerializer):
    """used to serialize the purchase orders"""
    quantity = serializers.IntegerField()

    class Meta:
        """meta class"""
        model = PurchaseOrder
        fields = ('po_number', 'vendor', 'items', 'quantity')

    def validate(self, attrs):
        """ used to validate the data """
        quantity = attrs.get('quantity', '')
        if quantity < 1:
            raise serializers.ValidationError(ERROR_MESSAGE['quantity-not-allowed'])
        return attrs

    def create(self, validated_data):
        """used to create the purchase order"""
        return super(PurchaseOrderSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        """used to update the po"""
        return super(PurchaseOrderSerializer, self).update(instance=instance, validated_data=validated_data)
