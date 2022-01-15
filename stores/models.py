from pyexpat import model
from django.db import models
from apis.models import User
from versatileimagefield.fields import VersatileImageField,PPOIField
from django.utils.translation import gettext as _
# Create your models here.


class Storetype(models.Model):
    type=models.CharField(max_length=225)
    class Meta:
        verbose_name = _("Storetype")
        verbose_name_plural = _("Storetypes")

    def __str__(self):
        return self.type



class Store(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    logo_image = VersatileImageField(blank=True,null=True,upload_to="Logos/",default='default.jpg',ppoi_field='logo_image_ppoi')
    logo_image_ppoi = PPOIField()
    banner_image = VersatileImageField(blank=True,null=True,upload_to="Banners/",default='default.jpg',ppoi_field='banner_image_ppoi')
    banner_image_ppoi = PPOIField()
    name=models.CharField(max_length=225)
    storetype=models.ForeignKey(Storetype, related_name="productypes",on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")

    def __str__(self):
        return self.name
