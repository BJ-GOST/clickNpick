from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='agency', null=False, blank=False, default=1)
    category = models.CharField(max_length=255, null=True, blank=False)
    units = models.CharField(max_length=255, null=True, blank=False)
    price = models.IntegerField(null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)




class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products', null=True, blank=False)
    image = CloudinaryField('Image', resource_type='auto', null=True, blank=False)


{
    "name":"sphagetti",
    "category":"food",
    "units":"packets",
    "price":23,
    "description":"Dawaat Pasta"
}