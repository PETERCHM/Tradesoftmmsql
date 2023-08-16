from rest_framework import generics
from .models import SourceOrders, Waitertab, Itemstab, Tablersv
from .serializers import SourceOrdersSerializer, WaitertabSerializer, ItemstabSerializer, TablersvSerializer

class SourceOrdersList(generics.ListCreateAPIView):
    queryset = SourceOrders.objects.all()
    serializer_class = SourceOrdersSerializer

class WaitertabList(generics.ListCreateAPIView):
    queryset = Waitertab.objects.all()
    serializer_class = WaitertabSerializer

class ItemstabList(generics.ListCreateAPIView):
    queryset = Itemstab.objects.all()
    serializer_class = ItemstabSerializer

class TablersvList(generics.ListCreateAPIView):
    queryset = Tablersv.objects.all()
    serializer_class = TablersvSerializer
