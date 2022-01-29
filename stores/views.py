from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Store,ProductType,AvailableProductType
from .serializers import StoreSerializer,ProductTypeSerializer
# Create your views here.



class StoreViewSet(viewsets.ModelViewSet):
     queryset = Store.objects.all()
     serializer_class = StoreSerializer

    

class ProductTypeViewSet(viewsets.ModelViewSet):
     queryset = ProductType.objects.all()
     serializer_class = ProductTypeSerializer

