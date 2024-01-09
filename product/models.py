from django.db import models

# Create your models here.

PRODUCT_FLAG = {
    ('Sale','sale'),
    ('Feature','feature'),
    ('New','new')
}

class Product(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product',default='default.png')
    flag = models.CharField(max_length=10,choices=PRODUCT_FLAG)
    price = models.FloatField()
    sku = models.IntegerField()
    brand = ''
    tags = ''
    subtitle = models.TextField(max_length=500)
    describtion = models.TextField(max_length=20000)
    '''
    name 
    flag 
    image 
    price
    sku
    brand
    tags
    subtitle
    describtion

    '''

class Produkt_images(models.Model):
    pass
    '''
    product
    image
    

    '''

class Brand(models.Model):
    pass
    '''
    name 
    image

    '''



class Reviews(models.Model):
    pass

    '''
    user
    product
    review
    date
    rate
    '''