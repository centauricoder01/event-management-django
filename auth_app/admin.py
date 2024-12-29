from django.contrib import admin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'mobile', 'organization')  # Fields to display in the list view
    search_fields = ('email', 'name')  # Fields that can be searched
    ordering = ('email',)  # Default ordering

admin.site.register(CustomUser, CustomUserAdmin)