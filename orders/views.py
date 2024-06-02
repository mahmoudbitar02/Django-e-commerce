from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Order,OrderDetail


class OrderList(ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 1


def add_to_cart(request):
    pass

def remove_from_cart(request):
    pass

def checkout(request):
    pass


def invoice(request):
    pass