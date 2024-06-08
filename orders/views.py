from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from datetime import datetime
# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Order,OrderDetail, Cart, CartDetail, Coupon
from product.models import Product

from django.http import JsonResponse
from django.template.loader import render_to_string

class OrderList(ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 1


def add_to_cart(request):
    quantity = request.POST['quantity']
    product = Product.objects.get(id=request.POST['product_id'])
    cart = Cart.objects.get(user=request.user,cart_status='Inprogress')
    cart_detail, crated = CartDetail.objects.get_or_create(cart=cart,product=product)
    cart_detail.quantity=quantity
    cart_detail.price=product.price
    cart_detail.total= round(int(quantity) * product.price ,2)
    cart_detail.save()
    return redirect(f'/products/{product.slug}')


def remove_from_cart(request,id):
    cart_detail = CartDetail.objects.get(id=id)
    cart_detail.delete()
    return redirect(f'/products')

def checkout(request):
    cart = Cart.objects.get(user=request.user,cart_status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)

    discount = 0
    delivery_fee = 50
    total = delivery_fee + cart.cart_total()
    sub_total = cart.cart_total()

    if  request.method == 'POST':
        code =request.POST['coupon']
        # coupon = Coupon.objects.get(code=code)
        coupon = get_object_or_404(Coupon, code=code)
        today_date = datetime.today().date()
        
        if coupon and coupon.quantity > 0:
            if today_date >= coupon.from_date and today_date <= coupon.to_date:
                code_value = cart.cart_total() / 100 * coupon.value
                discount = round(code_value,2)
                total = cart.cart_total() - code_value
                total = total + delivery_fee
                html = render_to_string('include/checkout_table.html',{'cart':cart,'cart_detail':cart_detail,'delivery_fee':delivery_fee,'total':total,'sub_total':sub_total,'discount':discount})
                return JsonResponse({'result':html})



    return render(request,'orders/checkout.html',{'cart':cart,'cart_detail':cart_detail,'delivery_fee':delivery_fee,'total':total,'sub_total':sub_total,'discount':discount})









def invoice(request):
    pass



