from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from drf_yasg.utils import swagger_auto_schema

# local imports
from apps.orders.filters import PurchaseOrderFilters
from apps.orders.messages import *
from apps.orders.serializers import *


class PurchaseOrderViewSet(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin):
    """
    order class viewset
    """
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()
    filterset_class = PurchaseOrderFilters

    def list(self, request, *args, **kwargs):
        """used to list all the orders with vendor filter"""
        queryset = self.get_queryset()
        filtered_query = self.filter_queryset(queryset=queryset)
        if filtered_query.exists():
            serializer = PurchaseOrderListSerializer(filtered_query, many=True)
            return Response({'data': serializer.data})
        return Response({'details': ERROR_MESSAGE['order_not_found']}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        """used to create an order"""
        serializer = PurchaseOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'details': SUCCESS_MESSAGE['order_created']})

    def retrieve(self, request, *args, **kwargs):
        """method to retrieve single instance of purchase order"""
        instance = self.get_queryset().filter(id=kwargs.get('pk')).first()
        if not instance:
            return Response({'details': ERROR_MESSAGE['not_found']}, status=status.HTTP_404_NOT_FOUND)
        serializer = PurchaseOrderListSerializer(instance)
        return Response({'data': serializer.data})

    @swagger_auto_schema(methods=['put'])
    def update(self, request, *args, **kwargs):
        """update the order details"""
        instance = self.get_queryset().filter(id=kwargs.get('pk')).first()
        if not instance:
            return Response({'details': ERROR_MESSAGE['not_found']}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer_class()(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'details': SUCCESS_MESSAGE['order_updated']})

    def destroy(self, request, *args, **kwargs):
        """Delete the purchase order"""
        instance = self.get_queryset().filter(id=kwargs.get('pk')).first()
        if not instance:
            return Response({'details': ERROR_MESSAGE['not_found']}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({'details': SUCCESS_MESSAGE['order_deleted']})

    @action(methods=['post'], detail=True, url_path='acknowledge', url_name='acknowledge',
            serializer_class=UpdateAcknowledgeSerializer)
    def update_acknowledgement_date(self, request, *args, **kwargs):
        """Update the acknowledgement date"""
        instance = self.get_queryset().filter(id=kwargs.get('pk')).first()
        if not instance:
            return Response({'details': ERROR_MESSAGE['not_found']}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer_class()(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'details': SUCCESS_MESSAGE['order_updated']})
