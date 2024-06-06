from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from drf_yasg.utils import swagger_auto_schema

# local imports
from apps.vendor.messages import SUCCESS_MESSAGE, ERROR_MESSAGE
from apps.vendor.models import Vendor, HistoricalPerformance
from apps.vendor.serializers import VendorSerializer, VendorListSerializer, VendorPerformanceSerializer


class VendorViewSet(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin):
    """
    vendor class viewset
    """
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()

    def list(self, request, *args, **kwargs):
        """used to list all the vendors"""
        queryset = self.get_queryset()
        serializer = VendorListSerializer(queryset, many=True)
        return Response({'data': serializer.data})

    def create(self, request, *args, **kwargs):
        """used to create a vendor"""
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'details': SUCCESS_MESSAGE['vendor-created']})

    def retrieve(self, request, *args, **kwargs):
        """method to retrieve single instance of vendor"""
        instance = self.get_queryset().filter(id=kwargs.get('pk')).first()
        if not instance:
            return Response({'details': ERROR_MESSAGE['not-found']}, status=status.HTTP_404_NOT_FOUND)
        serializer = VendorListSerializer(instance)
        return Response({'data': serializer.data})

    @swagger_auto_schema(methods=['put'])
    def update(self, request, *args, **kwargs):
        """update the vendor details"""
        instance = self.get_queryset().filter(id=kwargs.get('pk')).first()
        if not instance:
            return Response({'details': ERROR_MESSAGE['not-found']}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer_class()(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'details': SUCCESS_MESSAGE['vendor-updated']})

    def destroy(self, request, *args, **kwargs):
        """Delete the vendor permanently"""
        instance = self.get_queryset().filter(id=kwargs.get('pk')).first()
        if not instance:
            return Response({'details': ERROR_MESSAGE['not-found']}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({'details': SUCCESS_MESSAGE['vendor-deleted']})

    @action(methods=['get'], url_name='performance', url_path='performance', detail=True,
            serializer_class=VendorPerformanceSerializer, queryset=HistoricalPerformance.objects.all())
    def vendor_performance(self, request, *args, **kwargs):
        """used to list vendor performance metrics"""
        qs = self.get_queryset().filter(vendor=kwargs['pk'])
        if not qs.first():
            return Response({'details': ERROR_MESSAGE['performance-not-found']}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer_class()(qs, many=True)
        return Response({'data': serializer.data})
