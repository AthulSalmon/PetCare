from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .models import *


def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('/Guest/Login/')  
    else:
        form = CustomerForm()
    
    return render(request, 'Customer_registration.html', {'form': form})


def register_shop(request):
    if request.method == 'POST':
        form = ShopRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Guest/Login/')  
    else:
        form = ShopRegistrationForm()
    return render(request, 'Shop.html', {'form': form})



def home(request):
    return render(request,"Homepage.html")




def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            shop_boarding = Shop.objects.get(email=username, password=password, shop_type="bording")
            request.session["sid"] = shop_boarding.id
            request.session["uname"] = shop_boarding.shop_name
            request.session["role"] = "shop_boarding"
            messages.success(request, "Login successful!")
            return redirect("/Services/homepage/")  
        except Shop.DoesNotExist:
            try:
                shop = Shop.objects.get(email=username, password=password)
                request.session["sid"] = shop.id
                request.session["uname"] = shop.shop_name
                request.session["role"] = "shop"
                messages.success(request, "Login successful!")
                return redirect("/Shop/homepage/") 
            except Shop.DoesNotExist:
                try:
                    customer = Customer.objects.get(email=username, password=password)
                    request.session["cid"] = customer.id
                    request.session["uname"] = customer.full_name
                    request.session["role"] = "customer"
                    messages.success(request, "Login successful!")
                    return redirect("/Customer/homepage/")   
                except Customer.DoesNotExist:
                    messages.error(request, "Invalid email or password. Please try again.")
                    return redirect("/Guest/Login/")
    return render(request, "Login.html")



    
