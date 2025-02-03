from django.shortcuts import render,redirect,get_object_or_404
from Customer.models import *
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
def shomepage(request):
    return render(request,"ServiceHomepage.html")



def shop_bookings(request):
    shop_id = request.session.get("sid")  
    if not shop_id:
        return redirect('/Guest/Login/') 
    bookings = Boarding.objects.filter(shop_id=shop_id).select_related('pet', 'shop')
    return render(request, 'serviceviewbooking.html', {'bookings': bookings})




def update_shop_rate(request):
    if request.method == "POST":
        shop_id = request.session.get("sid")
        if not shop_id:
            messages.error(request, "You must be logged in as a shop owner to update the rate.")
            return redirect("/Guest/Login/")
        
        shop = Shop.objects.get(id=shop_id)
        new_rate = request.POST.get("rate")
        
        try:
            shop.rate = float(new_rate) 
            shop.save()
            messages.success(request, "Rate updated successfully!")
        except ValueError:
            messages.error(request, "Please enter a valid rate.")
        
        return redirect("/Services/homepage/")

    return render(request, "rate.html")


def update_booking_status(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(Boarding, id=booking_id)
        new_status = request.POST.get('status')  
        if new_status in ['Pending', 'Approved', 'Rejected']: 
            booking.status = new_status
            booking.save()  
        return redirect('/Services/booking/details/') 
    
def service_profile(request):
    if "role" not in request.session or request.session["role"] not in ["shop", "shop_boarding"]:
        messages.error(request, "Unauthorized access. Please log in as a shop owner.")
        return redirect("/Guest/Login/")  # Redirect to login page

    shop = get_object_or_404(Shop, id=request.session["sid"])
    return render(request, "service_profile.html", {"shop": shop})


def logout_page(request):
    logout(request)
    return redirect('/Guest/Login/')