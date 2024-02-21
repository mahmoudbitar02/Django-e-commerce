# views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Order, OrderDetail, Cart,CartDetail
from .serializers import CartSerializer
from django.contrib.auth.models import User

class CartDetailCreateApi(generics.GenericAPIView): # GenericAPIView damit wir die List,Detail,Crete bearbeiten können override
    serializer_class=CartSerializer
    queryset=Cart.objects.all()


    def get(self, request,*args, **kwargs):
        user_name=self.kwargs['username']
        user=User.objects(username=user_name)
        cart = Cart.objects.get(user=user,cart_status='Inprogress' )
        return Cart