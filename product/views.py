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
    

#class BrandDetail(ListView):
 #   model=Product
  #  paginate_by = 50

   # def get_queryset(self):
    #    brand = Brand.objects.get(slug=self.kwargs['slug'])
     #   queryset = Brand.objects.filter(brand=brand)
      #  return queryset
    
    #def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
      #  data = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
       # print(f'brand:{data.name}')
       # print(f'brand:{data.image}')

        #context["brand"] = data
        #return context
    
    
    