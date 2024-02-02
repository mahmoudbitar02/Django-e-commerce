from django.db import models

# Create your models here.


class Company (models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company')
    call_us = models.CharField(max_length=25)
    emal_us = models.EmailField()
    about = models.CharField(max_length=1000)

    fb_link = models.URLField(null=True,blank=True)
    x_link = models.URLField(null=True,blank=True)
    ins_link = models.URLField(null=True,blank=True)
    linkedin_link = models.URLField(null=True,blank=True)

    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)







