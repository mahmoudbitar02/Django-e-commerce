# form
from rest_framework import serializers
from .models import Order, OrderDetail, Cart,CartDetail

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'