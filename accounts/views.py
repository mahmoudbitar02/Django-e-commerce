from django.shortcuts import render
from .models import Profile, Address, ContactNumbers

# Create your views here.
def signup(request):
    pass

def activate_account(requesst):
    pass


def profile(request):
    profile = Profile.objects.get(user=request.user)
    address = Address.objects.filter(user=request.user)
    contact_numbers = ContactNumbers.objects.filter(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile,'address':address,'contact_numbers':contact_numbers})


def dashboard(request):
    pass