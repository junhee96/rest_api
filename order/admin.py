from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'products', 'register_date', 'quantity']
    list_display_links = ['user', 'products']
    search_fields = ['user', 'products']


