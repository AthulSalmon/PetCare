from django.db import models
from Guest.models import *
from Shop.models import *


# Create your models here.
class Pet(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)  
    breed = models.CharField(max_length=50, blank=True)
    age = models.IntegerField()
    health_notes = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    pet_pic=models.ImageField(upload_to="pet/")
    def __str__(self):
        return f"{self.name} ({self.breed})"



class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    no_product = models.IntegerField()
    payment_method = models.CharField(
        max_length=10,
        choices=[('COD', 'Cash on Delivery'), ('ONLINE', 'Online Payment')],
        default='COD'
    )
    payment_status = models.CharField(max_length=20, default="Pending")  # Pending, Completed
    status = models.CharField(max_length=20, default="Pending")  # Order status




class Boarding(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    shop= models.ForeignKey(Shop,on_delete=models.CASCADE)
    rate= models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, default="Pending")
    booked_date = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if self.start_date and self.end_date and self.shop:
            days = (self.end_date - self.start_date).days
            days = max(days, 0)
            self.rate = days * self.shop.rate 
        super(Boarding, self).save(*args, **kwargs)
    
    
