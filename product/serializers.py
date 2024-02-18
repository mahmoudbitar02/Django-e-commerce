# form
from rest_framework import serializers
from .models import Product,Brand,Produkt_images
from django.db.models.aggregates import Avg

class ProduktImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produkt_images
        fields=['image']


class ProductListSerializer(serializers.ModelSerializer):
    #brand= BrandSerializer()  # damit alle Brand-fields auf der api seite ersehtlich sind 
    brand = serializers.StringRelatedField() # hier wird nur der name des Brandes gezeigt 
    price_with_tax = serializers.SerializerMethodField()
    #price_with_tax = serializers.SerializerMethodField(method_name='myfunc')
    avg_rate=serializers.SerializerMethodField()
    review_count=serializers.SerializerMethodField()


    class Meta: 
        model=Product
        fields='__all__'

    def get_price_with_tax(self,product):
        return product.price*1.1

    #def myfunc(self,product):
     #   return product.price*1.1
    def get_avg_rate(self,product):
        avg = product.product_review.aggregate(rate_avg=Avg('rate'))
        avg_rate= avg['rate_avg']
        if avg_rate :
            avg_rate=round(avg_rate,2)
        else:
            avg_rate=0
        return avg_rate
    
    def get_review_count(self,product):
        reviews=product.product_review.all().count()
        return reviews


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




