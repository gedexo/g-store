from django.contrib import admin
from .models import Category,SubCategory,\
    Brand,Products,Options,Sizes



admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Products)
admin.site.register(Options)
admin.site.register(Sizes)
# Register your models here.
