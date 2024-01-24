from django.db import models
from django.utils import timezone
from product.models import Product

# Create your models here.

ORDER_STATUS =(
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped')
    ('Delivered','Delivered')
)

class Order(models.Model):
    order_code=models.CharField(max_length=10)
    user = ''
    order_status = models.CharField(max_length=12, choices=ORDER_STATUS,default='Recieved')
    delivery_date = models.DateTimeField(null=True,blank=True)
    order_date = models.DateTimeField(default=timezone.now)
    


class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)