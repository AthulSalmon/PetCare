from django.db import models

SHOP_TYPES=[('shop','Shop'),('bording','Bording Service')]
dis=[('ernakulam','Ernakulam'),('kollam','Kollam'),('idukki','Idukki')]


class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    place=models.CharField(max_length=100)
    district = models.CharField(max_length=20, choices=dis)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    photo=models.ImageField(upload_to="Customer_image/")
    proof=models.ImageField(upload_to="Customer_proof/")
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)


class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    shop_type = models.CharField(max_length=20, choices=SHOP_TYPES)
    address = models.TextField()
    place=models.CharField(max_length=100)
    rate=models.IntegerField(default=1)
    district = models.CharField(max_length=20, choices=dis)
    date_joined = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=100)
    proof=models.ImageField(upload_to="Shop_proof/")
    Logo=models.ImageField(upload_to="Shop_logo/")




