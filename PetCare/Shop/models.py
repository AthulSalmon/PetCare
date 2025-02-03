from django.db import models
from Guest.models import *

class tbl_product(models.Model):
    product_name= models.CharField(max_length=50)
    product_details= models.CharField(max_length=500)
    product_rate= models.CharField(max_length=50)
    product_photo = models.FileField(upload_to='Assets/ProductPhoto/')
    stock= models.IntegerField()
    shop= models.ForeignKey(Shop, on_delete=models.CASCADE)
    


    

