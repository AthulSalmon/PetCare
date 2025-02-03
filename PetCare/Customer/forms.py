from django import forms
from .models import *
from django.utils.timezone import now

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'type', 'breed', 'age', 'health_notes','pet_pic']
        # widgets = {
        #     'health_notes': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
        # }











class OrderForm(forms.ModelForm):
    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
        required=True
    )
    payment_method = forms.ChoiceField(
        choices=[
            ('COD', 'Cash on Delivery'),
            ('ONLINE', 'Online Payment'),
        ],
        required=True
    )

    class Meta:
        model = Order
        fields = ['quantity', 'payment_method']









class BoardingForm(forms.ModelForm):
    class Meta:
        model = Boarding
        fields = ['pet', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        today = now().date()  # Convert current datetime to date

        if start_date and start_date.date() < today:  # Convert to date before comparison
            raise forms.ValidationError("Start date cannot be in the past.")

        if end_date and end_date.date() <= start_date.date():  # Convert to date before comparison
            raise forms.ValidationError("End date must be after the start date.")

        return cleaned_data
pet = forms.ModelChoiceField(queryset=Pet.objects.all(), empty_label="Select a Pet")