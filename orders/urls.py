from django.urls import path
from .views import OrderList, add_to_cart, remove_from_cart,checkout,CreateCheckoutSessionView, payment_fail, payment_success

from .api import CartDetailCreateApi,OrderListApi, CreateOrder

app_name = 'orders'


urlpatterns = [
    path('',OrderList.as_view(),name='order_list'),
    path('add-to-cart',add_to_cart,name='add_to_cart'),
    path('remove-from-cart/<int:id>',remove_from_cart,name='remove_from_cart'),
    path('checkout',checkout,name='checkout'),
    path('payment/success',payment_success,name='payment_success'),
    path('payment/fail',payment_fail,name='payment_fail'),

    path('create_checkout_session/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),






    #api
    path('api/<str:username>/cart',CartDetailCreateApi.as_view(),name='cart detail'),
    path('api/<str:username>/order',OrderListApi.as_view(),name='order list'),
    path('api/<str:username>/create-order',CreateOrder.as_view(),name='create order'),


    

]
