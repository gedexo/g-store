from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import Store,ProductType,AvailableProductType



class StoreSerializer(serializers.ModelSerializer):
      class Meta:
          model=Store
          fields='__all__'
        

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
          model=ProductType
          fields='__all__'