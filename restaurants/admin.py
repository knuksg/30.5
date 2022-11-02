from django.contrib import admin
from .models import Restaurant

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'created_at', 'updated_at']
admin.site.register(Restaurant, RestaurantAdmin)