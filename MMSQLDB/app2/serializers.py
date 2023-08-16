from rest_framework import serializers
from .models import SourceOrders, Waitertab, Itemstab, Tablersv

class SourceOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceOrders
        fields = '__all__'

class WaitertabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitertab
        fields = '__all__'

class ItemstabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itemstab
        fields = '__all__'

class TablersvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablersv
        fields = '__all__'
