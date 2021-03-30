from django.contrib import admin
from .models import Product

 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'stock', 'price', 'shelf_life']
    list_display_links = ['name', 'manufacturer']
    search_fields = ['name', 'manufacturer']


