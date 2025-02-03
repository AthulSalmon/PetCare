from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from Customer.models import *
from django.contrib.auth import authenticate,login,logout


def homepage(request):
    return render(request,"shophomepage.html")

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)  
            shop_id = request.session.get("sid")  
            if shop_id:
                try:
                    product.shop = Shop.objects.get(id=shop_id) 
                    product.save() 
                    return redirect('/Shop/addproduct')
                except Shop.DoesNotExist:
                    messages.error(request, "Invalid shop session. Please log in again.")
                    return redirect('/Guest/Login/')
            else:
                messages.error(request, "No shop logged in. Please log in first.")
                return redirect('/Guest/Login/')
    else:
        form = ProductForm()
    shop_id = request.session.get("sid")
    if shop_id:
        products = tbl_product.objects.filter(shop_id=shop_id)
    else:
        products = []

    return render(request, 'product.html', {'form': form, 'products': products})




def delete_product(request, pk):
    product = get_object_or_404(tbl_product, id=pk)
    product.delete()
    return redirect('/Shop/addproduct/')

def update_product(request, pk):
    product = get_object_or_404(tbl_product, id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/Shop/addproduct/')
    else:
        form = ProductForm(instance=product)
    return render(request, 'updateproduct.html', {'form': form})



def order_details(request):
    shop_id = request.session.get("sid")
    if not shop_id:
        return redirect('/Guest/Login/')  
    order = Order.objects.filter(products__shop__id=shop_id)
    return render(request, 'shopvieworder.html', {'order': order})



def change_status(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, id=order_id)
        new_status = request.POST.get("status")
        order.status = new_status
        if new_status == "Delivered":
            order.payment_status = "Completed"
        order.save()
        return redirect('/Shop/order_details')  


def logout_page(request):
    logout(request)
    return redirect('/Guest/Login/')

def shop_profile(request):
    if "role" not in request.session or request.session["role"] not in ["shop", "shop_boarding"]:
        messages.error(request, "Unauthorized access. Please log in as a shop owner.")
        return redirect("/Guest/Login/")  # Redirect to login page
    shop = get_object_or_404(Shop, id=request.session["sid"])
    return render(request, "shop_profile.html", {"shop": shop})




def add_stock(request, product_id):
    product = get_object_or_404(tbl_product, id=product_id)
    
    if request.method == 'POST':
        try:
            additional_stock = int(request.POST.get('additional_stock', 0))
            if additional_stock < 0:
                messages.error(request, "Stock cannot be negative.")
            else:
                product.stock += additional_stock
                product.save()
                return redirect('/Shop/homepage/')  # Redirect to the product list or homepage
        except ValueError:
            messages.error(request, "Please enter a valid stock number.")

    return render(request, 'Add_stock.html', {'product': product})
