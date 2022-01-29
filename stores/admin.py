import imp
from django.contrib import admin
from .models import Store,ProductType,AvailableProductType
# Register your models here.

admin.site.register(Store)
admin.site.register(ProductType)
admin.site.register(AvailableProductType)