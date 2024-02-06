from django.urls import path

app_name = 'product'

from .views import ProductList, ProductDetail,BrandList,BrandDetail,query_debug,add_review

urlpatterns = [
    path('', ProductList.as_view(),name='product_list'),
    path('<slug:slug>', ProductDetail.as_view(),name='product_detail'),
    path('<slug:slug>/add-review' , add_review , name='add_review'),
    path('brands/', BrandList.as_view(),name='brand_list'),
    path('brands/<slug:slug>',BrandDetail.as_view(),name='brand_detail'),
    path('debug/',query_debug,name='debug')
]






