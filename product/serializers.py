# form
from rest_framework import serializers
from .models import Product,Brand,Produkt_images

class ProduktImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produkt_images
        fields=['image']


class ProductListSerializer(serializers.ModelSerializer):
    #brand= BrandSerializer()  # damit alle Brand-fields auf der api seite ersehtlich sind 
    brand = serializers.StringRelatedField() # hier wird nur der name des Brandes gezeigt 
    price_with_tax = serializers.SerializerMethodField()
    #price_with_tax = serializers.SerializerMethodField(method_name='myfunc')

    class Meta: 
        model=Product
        fields='__all__'

    def get_price_with_tax(self,product):
        return product.price*1.1

    #def myfunc(self,product):
     #   return product.price*1.1


class ProductDetailSerializer(serializers.ModelSerializer):
    images= ProduktImagesSerializer(source='product_image',many=True)
    brand = serializers.StringRelatedField() 


    class Meta: 
        model=Product
        fields='__all__'

 

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'



class BrandDetailSerializer(serializers.ModelSerializer):
    products=ProductListSerializer(source='product_brand',many=True)
    class Meta:
        model=Brand
        fields='__all__'




