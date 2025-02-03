from django.contrib import admin
from .models import *

class MasterAdmin(admin.ModelAdmin):
    exclude = ['date_joined']  

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


class CustomerAdmin(MasterAdmin):
    list_display = ['full_name', 'username', 'phone_number', 'place', 'district', 'email', 'is_admin', 'date_joined']
    search_fields = ['full_name', 'username', 'email', 'phone_number']
    list_filter = ['district', 'is_admin']
    ordering = ['date_joined']
    readonly_fields = ['date_joined']  
    fieldsets = (
        (None, {
            'fields': ('full_name', 'username', 'phone_number', 'email', 'address', 'place', 'district', 'password', 'photo', 'proof', 'is_admin')
        }),
    )



class ShopAdmin(MasterAdmin):
    list_display = ['shop_name', 'owner_name', 'contact_number', 'email', 'shop_type', 'place', 'district', 'date_joined']
    search_fields = ['shop_name', 'owner_name', 'email', 'contact_number']
    list_filter = ['shop_type', 'district']
    ordering = ['date_joined']
    readonly_fields = ['date_joined']  
    fieldsets = (
        (None, {
            'fields': ('shop_name', 'owner_name', 'contact_number', 'email', 'shop_type', 'address', 'place', 'district', 'password', 'proof')
        }),
    )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Shop, ShopAdmin)
