from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Order,OrderDetail


class OrderList(ListView):
    model = Order
    context_object_name = 'orders'
