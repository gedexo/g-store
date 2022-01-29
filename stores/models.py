from pyexpat import model
from statistics import mode
from django.db import models
from apis.models import User
from versatileimagefield.fields import VersatileImageField,PPOIField
from django.utils.translation import gettext as _
# Create your models here.






class Store(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    logo_image = VersatileImageField(blank=True,null=True,upload_to="Logos/",ppoi_field='logo_image_ppoi')
    logo_image_ppoi = PPOIField()
    banner_image = VersatileImageField(blank=True,null=True,upload_to="Banners/",ppoi_field='banner_image_ppoi')
    banner_image_ppoi = PPOIField()
    name=models.CharField(max_length=225)
    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")

    def __str__(self):
        return self.name

## Available Product Types (Fashion, Mobile shop , etc )
class ProductType(models.Model):
    productType=models.CharField(max_length=225)


class AvailableProductType(models.Model):
    store=models.ForeignKey(Store,related_name='availableproducttypes',on_delete=models.CASCADE)
    type=models.ForeignKey(ProductType,related_name='availableproducttypes',on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("Storetype")
        verbose_name_plural = _("Storetypes")

    def __str__(self):
        return self.type.productType+"_SHOP"