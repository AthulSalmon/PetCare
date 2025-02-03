from django.urls import path
from .import views


urlpatterns = [
    path('homepage/',views.shomepage,name='shomepage'),
    path('booking/details/', views.shop_bookings, name='booking_details'),
    path('update_rate/', views.update_shop_rate, name='update_rate'),
    path('service_profile/', views.service_profile, name='service_profile'),
    path('bookings/update-status/<int:booking_id>/', views.update_booking_status, name='update_booking_status'),
    path('logout/',views.logout_page,name='logout'),

    
]