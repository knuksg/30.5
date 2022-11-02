from django import forms
from .models import Story

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'subtitle', 'main_image', 'content', ]
        widgets = {
            'content': SummernoteWidget(),
        }