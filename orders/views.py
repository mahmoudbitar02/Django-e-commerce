from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from datetime import datetime
# Create your views here.
from django.views.generic import ListView,DetailView, View
from .models import Order,OrderDetail, Cart, CartDetail, Coupon
from product.models import Product

from django.http import JsonResponse
from django.template.loader import render_to_string
import stripe

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
                html = render_to_string('include/checkout_table.html',{'cart':cart,'cart_detail':cart_detail,'delivery_fee':delivery_fee,'total':total,'sub_total':sub_total,'discount':discount,'code_value':code_value})
                return JsonResponse({'result':html})



    return render(request,'orders/checkout.html',{'cart':cart,'cart_detail':cart_detail,'delivery_fee':delivery_fee,'total':total,'sub_total':sub_total,'discount':discount})









class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        # Get the amount from the POST data
        amount = request.POST.get('amount')
        stripe.api_key = 'sk_test_51QG0QgCQpBZYDCacrom4c5kOweK2r1Knhr4J9gYSeJtkNfIex23B3nOJU4uWfdgc8FGhXv9nZQ3ZukW4Qne2YxSn00mI69AUNv'
        # Create a new Checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': amount,
                    'product_data': {
                        'name': 'Your Product Name',
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/orders/payment/success',
            cancel_url='http://127.0.0.1:8000/orders/payment/fail',
        )

        # Return the session ID as a JSON response
        return JsonResponse({'sessionId': session.id})


def payment_success(request):
    cart = Cart.objects.get(user = request.user, cart_status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    
    new_order=Order.objects.create(user = request.user)
    for item in cart_detail:
        OrderDetail.objects.create(
            order = new_order,
            product = item.product,
            price = item.price,
            quantity=item.quantity,
            total=item.total,
        )
    cart.cart_status='Completed'
    cart.save()
    return redirect('/')
def payment_fail(request):

    pass

