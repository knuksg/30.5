from django.contrib import admin
from .models import Restaurant

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'address', 'shop_number', 'between_pay', 'opening_time', 'created_at', 'updated_at']
admin.site.register(Restaurant, RestaurantAdmin)