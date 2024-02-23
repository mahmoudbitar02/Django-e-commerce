# views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Order, OrderDetail, Cart,CartDetail
from product.models import Product
from .serializers import CartSerializer, CartDetailSerializer
from django.contrib.auth.models import User

class CartDetailCreateApi(generics.GenericAPIView): # GenericAPIView damit wir die List,Detail,Crete bearbeiten können override
    serializer_class=CartDetailSerializer
    def get(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart, created=Cart.objects.get_or_create(user=user,cart_status='Inprogress')
        data=CartSerializer(cart).data
        return Response({'cart':data})


    def post(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])

        product=Product.objects.get(id=request.data['product_id'])
        quantity= int(request.data['quantity'])

        cart=Cart.objects.get(user=user,cart_status='Inprogress')
        cart_data,created=CartDetail.objects.get_or_create(cart=cart, product=product )
        cart_data.price=product.price
        cart_data.quantity=quantity
        cart_data.total= round (quantity*product.price,2)
        cart_data.save()
        return Response ({'status':200})
    

    def delete(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        product=Product.objects.get(id=request.data['product_id'])
        cart=Cart.objects.get(user=user,cart_status='Inprogress')
        cart_data=CartDetail.objects.get(cart=cart ,product=product)
        cart_data.delete()
        return Response ({'status':200, 'Messege':'deleted successfully'})
    



