from django.contrib import admin
from .models import tbl_product

@admin.register(tbl_product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_rate', 'stock', 'shop')
    search_fields = ('product_name', 'shop__shop_name')  # Assuming Shop model has shop_name
    list_filter = ('shop',)
