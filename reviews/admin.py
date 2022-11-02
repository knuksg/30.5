from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'user', 'rating', 'created_at', 'updated_at']
admin.site.register(Review, ReviewAdmin)