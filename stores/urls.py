
from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework import routers
app_name = 'stores'

router=routers.DefaultRouter()
router.register('stores',StoreViewSet)
router.register('producttype',ProductTypeViewSet)

urlpatterns = [
     path('', include(router.urls)),
]
