from django.contrib import admin
from .models import Order, Boarding

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'products', 'total_price', 'order_date', 'no_product', 'payment_method', 'payment_status', 'status')
    search_fields = ('user__name', 'products__product_name')
    list_filter = ('payment_status', 'status', 'payment_method')
    ordering = ('-order_date',)

@admin.register(Boarding)
class BoardingAdmin(admin.ModelAdmin):
    list_display = ('pet', 'shop', 'rate', 'start_date', 'end_date', 'status', 'booked_date')
    search_fields = ('pet__name', 'shop__shop_name')  # Assuming Pet and Shop models have 'name' fields
    list_filter = ('status',)
    ordering = ('-booked_date',)
