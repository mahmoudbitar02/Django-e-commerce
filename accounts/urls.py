from django.urls import path
from .views import signup, profile
app_name='accounts'

urlpatterns = [
    path('profile/',profile, name = 'profile'),
    path('singup/',signup, name = 'signup'),

]
