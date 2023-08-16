from django.urls import path
from .views import SourceOrdersList, WaitertabList, ItemstabList, TablersvList

urlpatterns = [
    path('source-orders/', SourceOrdersList.as_view(), name='source-orders-list'),
    path('waitertabs/', WaitertabList.as_view(), name='waitertabs-list'),
    path('itemstabs/', ItemstabList.as_view(), name='itemstabs-list'),
    path('tablersv/', TablersvList.as_view(), name='tablersv-list'),
]
