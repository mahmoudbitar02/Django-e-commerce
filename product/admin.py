from django.contrib import admin

# Register your models here.
from .models import Product, Produkt_images, Brand, Reviews
from tof.admin import TofAdmin, TranslationTabularInline


class ProductImagesAdmin (admin.TabularInline):
    model = Produkt_images

class ProductAdmin(TofAdmin):
    list_display=['id','name','brand','price','subtitle']
    list_filter=['brand','price']
    inlines = [ProductImagesAdmin,TranslationTabularInline]
    search_fields = ['name','subtitle','describtion']
    list_editable = ['name','brand','price']
    

class RewiewAdmin(admin.ModelAdmin):
    list_display=['user','product','rate','comment','created_at']
    list_filter=['created_at','rate']
    search_fields = ['comment','rate',]







admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Reviews,RewiewAdmin)











