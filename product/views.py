from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Count
from .models import Product,Produkt_images,Brand,Reviews

# Create your views here.


class ProductList(ListView):
    model = Product
    paginate_by = 50


class ProductDetail(DetailView):
    model = Product
    

class BrandList(ListView):
    model= Brand
    queryset = Brand.objects.all().annotate(product_count=Count('product_brand'))
    paginate_by = 50


class BrandDetail(DetailView):
    model = Brand
    #queryset = Brand.objects.filter(slug=slug).annotate(product_count=Count('product_brand'))

    def get_queryset(self):
        queryset = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))

        return queryset
    