from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path,include
from . views import *

app_name = 'apis'

urlpatterns = [
    path('create-user/',CreateUserView.as_view(),name='create'),
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
