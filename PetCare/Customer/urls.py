from django.urls import path
from . import views

urlpatterns = [
    path("homepage/", views.customer_homepage, name="customer_homepage"),
    path('logout/',views.logout_page,name='logout'),
    path('add/', views.add_pet, name='add_pet'),
    path('list/', views.pet_list, name='pet_list'),
    path('edit-pet/<int:pet_id>/', views.edit_pet, name='edit_pet'),
    path('delete-pet/<int:pet_id>/', views.delete_pet, name='delete_pet'),
    path('products/', views.product_display, name='product_display'),
    # path('order-now/<int:product_id>/', views.order_now, name='order_now'),
    # path('order-success/', views.order_success, name='order_success'),
    # path('payment/<int:order_id>/', views.payment_page, name='payment_page'),
      # URL for displaying product details and placing the order
    path('order/<int:product_id>/', views.order_now, name='order_now'),

    # URL for order success page
    path('order-success/', views.order_success, name='order_success'),

    path('payment-gateway/',views.payment_gateway, name='payment_gateway'),

    # URL for the product display page (where all products are listed)
    path('product-display/', views.product_display, name='product_display'),


    path('customer_order_details', views.customer_order_details, name='customer_order_details'),

     path('book-boarding/<int:shop_id>/',views.create_boarding, name='book_boarding'),
    path('boarding_list/', views.customer_booking_details, name='boarding_list'),
    path('viewshop/', views.customer_view_shop, name='viewshop'),
    path('customer_profile/', views.customer_profile, name='customer_profile'),
]
