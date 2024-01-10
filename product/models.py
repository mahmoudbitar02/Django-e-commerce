from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

PRODUCT_FLAG = {
    ('Sale','sale'),
    ('Feature','feature'),
    ('New','new')
}

class Product(models.Model):
    
    name = models.CharField(_('name'), max_length=100)
    image = models.ImageField(_('image'),upload_to='product',default='default.png')
    flag = models.CharField(_('flag'),max_length=10,choices=PRODUCT_FLAG)
    price = models.FloatField(_('price'))
    sku = models.IntegerField(_('sku'))
    brand = models.ForeignKey('brand',verbose_name=_('brand'),related_name='product_brand',on_delete=models.CASCADE)
    tags = TaggableManager()
    subtitle = models.TextField(_('sbtitle'),max_length=500)
    describtion = models.TextField(_('describtion'),max_length=20000)
    def __str__(self):
        return self.name

class Produkt_images(models.Model):
    pass
    '''
    product
    image
    

    '''

class Brand(models.Model):
    
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