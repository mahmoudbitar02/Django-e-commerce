# form
from rest_framework import serializers
from .models import Product,Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'



class ProductSerializer(serializers.ModelSerializer):
    #brand= BrandSerializer()  # damit alle Brand-fields auf der api seite ersehtlich sind 
    brand = serializers.StringRelatedField() # hier wird nur der name des Brandes gezeigt 
    class Meta: 
        model=Product
        fields='__all__'
