from rest_framework import serializers 
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['timestamp', 'seller']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image 
        exclude = ['product']


