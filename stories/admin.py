from django.contrib import admin
from .models import Story

# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'subtitle', 'created_at', 'updated_at']
admin.site.register(Story, StoryAdmin)