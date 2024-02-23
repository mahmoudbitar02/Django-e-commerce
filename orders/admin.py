from django.contrib import admin

# Register your models here.
from .models import Order,OrderDetail,Cart,CartDetail

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_code','order_status','order_date','delivery_date']
    list_filter = ['order_code','order_status']


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order','product','price','total']
    list_filter = ['price','quantity']

class CartDetailAdmin(admin.ModelAdmin):
    list_display= ['id','cart','product_id']


admin.site.register(Order,OrderAdmin)
admin.site.register(OrderDetail,OrderDetailAdmin)
admin.site.register(Cart)
admin.site.register(CartDetail,CartDetailAdmin)

