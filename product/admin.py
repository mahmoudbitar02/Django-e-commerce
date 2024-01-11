from django.contrib import admin

# Register your models here.
from .models import Product, Produkt_images, Brand, Reviews

admin.site.register(Product)
admin.site.register(Produkt_images)
admin.site.register(Brand)
admin.site.register(Reviews)





