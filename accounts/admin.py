from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'nickname', 'phone', 'address', 'gender']
    list_display_links = ['username', 'nickname']
    search_fields = ['username', 'nickname']


