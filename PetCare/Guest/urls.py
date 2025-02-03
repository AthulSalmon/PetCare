from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('Register/',views.register_customer,name="register_customer"),
    path('ShopRegister/',views.register_shop,name="register_shop"),
    path("Login/", views.Login, name="Login"),
    
]