from django.urls import path

app_name = 'product'

from .views import ProductList, ProductDetail,BrandList,BrandDetail,query_debug

urlpatterns = [
    path('', ProductList.as_view(),name='product_list'),
    path('<slug:slug>', ProductDetail.as_view(),name='product_detail'),
    path('brands/', BrandList.as_view(),name='brand_list'),
    path('brands/<slug:slug>',BrandDetail.as_view(),name='brand_detail'),
    path('debug/',query_debug,name='debug')
]






