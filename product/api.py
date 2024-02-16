# views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def productlist_api(request):
    products=Product.objects.all()[:100]
    data=ProductSerializer(products,many=True, context={'request':request}).data
    return Response({'data':data})



class ProductListApi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer