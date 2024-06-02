from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Order,OrderDetail, Cart, CartDetail
from product.models import Product


class OrderList(ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 1


def add_to_cart(request):
    quantity = request.POST['quantity'] # or request.POST.get('quantity') it is the same think
    product = Product.objects.get(id=request.POST['product_id'])
    cart = Cart.objects.get(user=request.user, cart_status = 'Inprogress')
    cart_detail,created = CartDetail.objects.get_or_create(cart=cart,product=product)
    cart_detail.quantity = quantity
    cart_detail.price = product.price
    cart_detail.total = round(int(quantity) * product.price,2)
    cart_detail.save()
    return redirect(f'/products/{product.slug}')

def remove_from_cart(request):
    pass

def checkout(request):
    pass


def invoice(request):
    pass