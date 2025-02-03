from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = tbl_product
        fields = ['product_name', 'product_details', 'product_rate','stock', 'product_photo']  # Exclude 'shop'
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'product_details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter product details'}),
            'product_rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product rate'}),
             'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of items'}),
            'product_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

