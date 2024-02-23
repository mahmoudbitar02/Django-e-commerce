# form
from rest_framework import serializers
from .models import Order, OrderDetail, Cart,CartDetail


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartDetail
        fields=['id','price','product','quantity','total']


class CartSerializer(serializers.ModelSerializer):
    cart_detail=CartDetailSerializer(many=True)#wenn cart_detail = der name vom dem relation muss hier kein Source hinzugefügt (source=cart_detail,many=True)
    class Meta:
        model=Cart
        fields='__all__'