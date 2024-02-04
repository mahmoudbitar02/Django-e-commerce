from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Count
from .models import Product,Produkt_images,Brand,Reviews
from django.db.models import Q,F
# Create your views here.


def query_debug (request):
    #data=Product.objects.filter(price__lte=55.83) # weniger oder gleich
    #data=Product.objects.filter(price__gte=55.83) # großer oder gleich
    #data=Product.objects.filter(price__range=(20,24)) # range
    #data=Product.objects.filter(brand__id=5) # id
    #data=Product.objects.filter(brand__id__gt=5) # id 5 oder großer als 5   Dustin
    #data=Product.objects.filter(name__contains='Dustin') # name enthält Dusten   
    #data=Product.objects.filter(name__startswith='Dustin') # name startet mit Dusten
    #data=Product.objects.filter(name__endswith='Cisneros') # name endet mit Cisneros
    #data=Product.objects.filter(name__isnull=True) # kein name vorhanden zu einem Product  
    #data=Product.objects.filter(name__contains='Dustin',price__gt=50) # name dustein und price großer als 50
    #data=Product.objects.filter(Q(name__contains='Dustin') | Q(price__gt=50)) # name Dusten or price großer als 50 (|=or) WICHTIG: import Q 
    #data=Product.objects.filter(Q(name__contains='Dustin') & Q(price__gt=50)) # name Dusten und price großer als 50 (&=and) WICHTIG import Q
    #data=Product.objects.filter(price=F('quantity')) # spaltenwert Price = spaltenwert quantity WICHTIG: import F
    data=Product.objects.all().order_by('-name') # sortieren aufsteigend ohne (-), absteigend mit (-) vor dem name
    return render(request,'product/productlist.html',{'data':data})

class ProductList(ListView):
    model = Product
    paginate_by = 50


class ProductDetail(DetailView):
    model = Product
    

class BrandList(ListView):
    model= Brand
    queryset = Brand.objects.all().annotate(product_count=Count('product_brand'))
    paginate_by = 50


#class BrandDetail(DetailView):
 #   model = Brand
    #queryset = Brand.objects.filter(slug=slug).annotate(product_count=Count('product_brand'))

  #  def get_queryset(self):
   #     queryset = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))
    #    return queryset
    

class BrandDetail(ListView):
    model=Product
    paginate_by = 20
    template_name ='product/brand_detail.html'

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        print(f'brand:{data.name}')
        print(f'brand:{data.image}')

        context["brand"] = data
        return context
    
    
    