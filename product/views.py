from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Product,Produkt_images,Brand,Reviews
from django.db.models import Q,F,Value,Func
from django.db.models.aggregates import Sum, Avg, Min, Max, Count
from django.db.models.functions import Concat
from django.db.models import ExpressionWrapper,DecimalField,FloatField
from.forms import ProductReviewForm
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
    #data=Product.objects.all().order_by('-name') # sortieren aufsteigend ohne (-), absteigend mit (-) vor dem name
    #data=Product.objects.earliest('name') # sortiert und brngt der erste Name WICHTIG: kein loop in html
    #data=Product.objects.latest('name') #sortiert und brngt der letzte Name WICHTIG: kein loop in html
    #data=Product.objects.values_list('name','price','brand') # bestimmte spalten holen// .distinct() = kein mehrmalig
    #data=Product.objects.only('name','id',) # holt nur der Name und ID aufpassen beim loop verwenden!!
    #data=Product.objects.defer('brand') # ausschließen brand
    #data=Product.objects.select_related('brand').all() # select_related = brand wird mit dem selber Query angeschlossen, d.h. query geht einmal und holt die Daten aus dem DB, andersrum wird zu jedem Product ein query gemacht um den Brand aus dem DB zu holen(nur bei Foreignkey oder one to one relation)
    #data=Product.objects.prefetch_related('brand').all() # select_related = brand wird mit dem selber Query angeschlossen, d.h. query geht einmal und holt die Daten aus dem DB, andersrum wird zu jedem Product ein query gemacht um den Brand aus dem DB zu holen(nur bei many to many relation)
    #data=Product.objects.aggregate(min_price=Min('price'),avg_peice=Avg('price')) # plus minus max min etc. 
    #data=Product.objects.annotate(is_new=Value(True)) # füge eine neue Spalte mit der Value True
    #data=Product.objects.annotate(is_new=F('quantity')+1 -1 *2) # man kann die felder beliebig gestalten 
    #data=Product.objects.annotate(
     #   full_name= Concat('name',Value(' '),'flag') # zwei spalten zusammenführen WICHTIG: import Concat 
    #)

    dis_price=ExpressionWrapper(F('price')*.8,output_field=DecimalField()) 
    data=Product.objects.annotate(discount_price=dis_price) # füge neue Spalte mit dem neuen Prise 




    return render(request,'product/productlist.html',{'data':data})

class ProductList(ListView):
    model = Product
    paginate_by = 50


class ProductDetail(DetailView):
    model = Product



def add_review(request,slug):
    product=Product.objects.get(slug=slug)
    if request.method=='POST':
        form= ProductReviewForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.User = request.user  
            myform.product=product
            myform.save()
    return redirect(f'/products/{product.slug}')


    


    

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
    
    


