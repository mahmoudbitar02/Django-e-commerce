from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User
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
    brand = models.ForeignKey('Brand',verbose_name=_('brand'),related_name='product_brand',on_delete=models.CASCADE)
    tags = TaggableManager()
    subtitle = models.TextField(_('sbtitle'),max_length=500)
    describtion = models.TextField(_('describtion'),max_length=20000)
    slug =models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name

class Produkt_images(models.Model):
    product = models.ForeignKey(Product,verbose_name= _('product'), related_name='product_image', on_delete=models.CASCADE)
    image =models.ImageField(_('image'),uplode_to='product_image')
    def __str__ (self):
        return str(self.product)

class Brand(models.Model):
    name = models.CharField(_('name'), max_length=100)
    image = image =models.ImageField(_('image'),uplode_to='brand')
    def __str__ (self):
        return self.name



class Reviews(models.Model):
    user = models.ForeignKey(User,verbose_name=_('user'),related_name='review_author',on_delete=models.SET_NULL, null=True,blank=True)
    product = models.ForeignKey(Product,verbose_name= _('product'), related_name='product_review', on_delete=models.CASCADE)
    comment = models.CharField(_('comment'),max_length=200)
    rate = models.IntegerField(-('rate'))
    created_at = models.DateTimeField(default=timezone.now)
    def __str__ (self):
        return str(self.product)
    