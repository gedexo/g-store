import imp
from locale import currency
from statistics import mode
from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from stores.models import AvailableProductType
# Create your models here.
class Category(models.Model):
    productType=models.ForeignKey(AvailableProductType,related_name='categories',on_delete=models.CASCADE)
    name=models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    order=models.IntegerField()
    image=VersatileImageField(blank=True,null=True,upload_to="fashion/Subcategory/",ppoi_field='image_ppoi')
    image_ppoi = PPOIField()    
    name=models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['order']


class Brand(models.Model):
    name = models.CharField(max_length = 225)
    is_popular =models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Products(models.Model):
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE,null=True)
    order=models.IntegerField()
    image=VersatileImageField(blank=True,null=True,upload_to="fashion/Products/",ppoi_field='image_ppoi')
    image_ppoi = PPOIField()
    name=models.CharField(max_length = 200,default='Product Name')
    productprice=models.BigIntegerField(default=0)
    currency=models.CharField(max_length = 100,default='INR')
    created_date=models.DateTimeField(auto_now=True)
    stock=models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Options(models.Model):
    product = models.ForeignKey(Products, related_name='options', on_delete=models.CASCADE)
    order=models.IntegerField()
    image_one=VersatileImageField(blank=True,null=True,upload_to="fashion/Options/",ppoi_field='image_one_ppoi')
    image_one_ppoi = PPOIField()
    image_two=VersatileImageField(blank=True,null=True,upload_to="fashion/Options/",ppoi_field='image_two_ppoi')
    image_two_ppoi = PPOIField()
    image_three=VersatileImageField(blank=True,null=True,upload_to="fashion/Options/",ppoi_field='image_three_ppoi')
    image_three_ppoi = PPOIField()
    color=models.CharField(max_length = 200)
    colorhash=models.CharField(max_length = 200)
    stock=models.IntegerField(null=True)
    def __str__(self):
        return self.color

    class Meta:
        ordering = ['order']

class Sizes(models.Model):
    option = models.ForeignKey(Options, related_name='sizes', on_delete=models.CASCADE)
    size=models.CharField(max_length = 200,null=True,blank=True)
    stock=models.IntegerField(null=True)

    def __str__(self):
        return self.size