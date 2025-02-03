from django import forms
from .models import Customer, Shop

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'username', 'phone_number', 'address', 'district', 'place', 'email', 'password', 'photo', 'proof']
        widgets = {
            'password': forms.PasswordInput(),  # Password field rendered as a password input
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'proof': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ShopRegistrationForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['shop_name', 'owner_name', 'contact_number', 'email', 'shop_type', 'address', 'password', 'proof', 'Logo', 'district', 'place']
        widgets = {
            'password': forms.PasswordInput(),  # Password field rendered as a password input
            'proof': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'Logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
