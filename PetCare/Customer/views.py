from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from Shop.models import *
from Customer.models import *
from Guest.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal
from django.contrib.auth import authenticate,login,logout


def customer_homepage(request):
    if not request.session.get("cid"):
        return redirect("/Guest/Login/")
    customer_name = request.session.get("uname", "Customer")
    return render(request, "customerhomepage.html", {"customer_name": customer_name})

def logout_page(request):
    logout(request)
    return redirect('/Guest/Login/')

# def product_display(request):
#     products = tbl_product.objects.all()
#     return render(request, "productdisplay.html", {"products": products})

def customer_profile(request):
    if "role" not in request.session or request.session["role"] != "customer":
        messages.error(request, "Unauthorized access. Please log in as a customer.")
        return redirect("/Guest/Login/")  # Redirect to login page

    customer = get_object_or_404(Customer, id=request.session["cid"])
    return render(request, "customer_profile.html", {"customer": customer})


def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)  
        if form.is_valid():
            pet = form.save(commit=False)
            try:
                customer = Customer.objects.get(id=request.session["cid"])
                pet.owner = customer
                pet.save()
                return redirect('/Customer/homepage/')
            except Customer.DoesNotExist:
                messages.error(request, "Customer not found. Please log in again.")
                return redirect('/Guest/Login/')
        else:
            # Log or display form errors for debugging
            print(form.errors)
            messages.error(request, "Please correct the errors below.")
    else:
        form = PetForm()
    print(form.errors)

    return render(request, 'addpet.html', {'form': form})





def pet_list(request):
    try:
        username = request.session.get('cid')  
        if not username:
            return HttpResponse("User is not logged in.", status=403)

        pets = Pet.objects.all()  
        return render(request, 'listpet.html', {'pets':pets})
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)
    
def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        pet.delete()
        return redirect('/Customer/list/')
    return render(request, 'deletepet.html', {'pet': pet})


def edit_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)   
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('/Customer/list/')
    else:
        form = PetForm(instance=pet)
    return render(request, 'edit_pet.html', {'form': form, 'pet': pet})






def product_display(request):
    products = tbl_product.objects.all()
    for product in products:
        if product.stock == 0:
            product.status_message = "Out of stock"
        elif product.stock < 10:
            product.status_message = "Few left"
        else:
            product.status_message = "In stock"
    return render(request, "productdisplay.html", {"products": products})







def order_now(request, product_id):
    product = get_object_or_404(tbl_product, id=product_id)

    try:
        customer = Customer.objects.get(id=request.session.get("cid"))
    except Customer.DoesNotExist:
        return redirect('/Customer/homepage/')

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            payment_method = form.cleaned_data['payment_method']

            # Validate stock
            if quantity > product.stock:
                messages.error(request, "Not enough stock available.")
                return redirect(request.path)

            total_price = Decimal(product.product_rate) * quantity

            # Validate total price
            if total_price > Decimal('99999999.99'):
                messages.error(request, "Total price exceeds the maximum allowed value.")
                return redirect(request.path)

            # Create order
            order = Order.objects.create(
                user=customer,
                products=product,
                total_price=total_price,
                no_product=quantity,
                payment_method=payment_method,
                payment_status="Pending" if payment_method == "ONLINE" else "Completed",
                status="Pending"
            )

            # Update stock
            product.stock -= quantity
            product.save()

            # Redirect based on payment method
            if payment_method == "ONLINE":
                return redirect('/Customer/payment-gateway/?order_id={}'.format(order.id))
            else:
                messages.success(request, "Order placed successfully!")
                return redirect('/Customer/order-success/')
    else:
        form = OrderForm()

    return render(request, "order_now.html", {
        "product": product,
        "form": form,
    })


def payment_gateway(request):
    order_id = request.GET.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        # Simulate successful payment (use a real payment gateway here)
        order.payment_status = "Completed"
        order.save()
        messages.success(request, "Payment successful!")
        return redirect('/Customer/order-success/')

    return render(request, "payment.html", {"order": order})




def order_success(request):
    return render(request, 'order_success.html')


def customer_order_details(request):
    customer = Customer.objects.get(id=request.session["cid"]) 
    order = Order.objects.filter(user=customer)
    return render(request, 'vieworder.html', {'order': order})


def customer_view_shop(request):
    shop=Shop.objects.filter(shop_type='bording')
    return render(request,'viewshop.html',{'shop':shop})
    





def create_boarding(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)

    if request.method == 'POST':
        form = BoardingForm(request.POST)
        if form.is_valid():
            boarding = form.save(commit=False)
            boarding.shop = shop
            boarding.rate = shop.rate  
            boarding.save()  
            return redirect('/Customer/homepage/')
        else:
            print(form.errors)
    else:
        form = BoardingForm()

    return render(request, 'Book_boarding.html', {'form': form, 'shop': shop})



def customer_booking_details(request):
    customer = Customer.objects.get(id=request.session["cid"]) 
    boarding = Boarding.objects.filter(pet__owner=customer)
    return render(request, 'viewbooking.html', {'boardings': boarding})




# def payment_method_selection(request, product_id):
#     product = tbl_product.objects.get(id=product_id)
#     if request.method == 'POST':
#         # Handle Cash on Delivery selection
#         if 'cash_on_delivery' in request.POST:
#             return redirect('confirm_order', product_id=product.id)
#         # Handle Online Payment selection
#         elif 'online_payment' in request.POST:
#             return redirect('payment_page')
#     return render(request, 'payment_method_selection.html', {'product': product})

# # Order Confirmation (for Cash on Delivery)
# def confirm_order(request, product_id):
#     product = tbl_product.objects.get(id=product_id)
#     if request.method == 'POST':
#         # Create an order with "Cash on Delivery" method
#         order = Order.objects.create(
#             product=product,
#             payment_method="COD",
#             status="Pending"
#         )
#         messages.success(request, "Your order has been placed successfully!")
#         return redirect('customer_homepage')
#     return render(request, 'order_confirmation.html', {'product': product})

# def payment_page(request):
#     if request.method == 'POST':
#         order = Order.objects.create(
#             product=tbl_product.objects.get(id=request.POST.get('product_id')),
#             payment_method="Online",
#             status="Paid"
#         )
#         messages.success(request, "Payment successful!")
#         return redirect('/Customer/customer_homepage/')
#     return render(request, 'payment_page.html')
