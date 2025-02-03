from django.urls import path
from . import views

urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('logout/',views.logout_page,name='logout'),

    
    path('addproduct/', views.add_product, name='addproduct'),
    path('order_details', views.order_details, name='order_details'),
    path('order/status/<int:order_id>/', views.change_status, name='change_status'),

    path('delete-product/<int:pk>/', views.delete_product, name='delete_product'),
    path('update-product/<int:pk>/', views.update_product, name='update_product'),

    path('shop_profile/', views.shop_profile, name='shop_profile'),
    path('add_stock/<int:product_id>/', views.add_stock, name='add_stock'),

]
