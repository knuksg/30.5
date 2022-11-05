from .models import Review, ReviewImage
from django import forms
from django.forms import Textarea, TextInput, ImageField, FileInput


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["content", "rating"]
        labels = {
            "content": "",
            "rating": "별점",
        }
        widgets = {
            "content": Textarea(
                attrs={
                    "style": "color: #adb5bd;",
                    "placeholder": "주문하신 메뉴는 어떠셨나요? 식당의 분위기와 서비스도 궁금해요!",
                }
            )
        }


class ReviewImageForm(forms.ModelForm):
    class Meta:
        model = ReviewImage
        fields = [
            "photo1",
            "photo2",
            "photo3",
        ]
        labels = {
            "photo1": "이미지 추가",
            "photo2": "",
            "photo3": "",
        }
        widgets = {
            "photo1": FileInput(
                attrs={
                    "id": "image_field",
                    "style": "height: 100px; width: 100px; border: 1px dashed #adb5bd; color: #adb5bd;",
                }
            ),
            "photo2": FileInput(
                attrs={
                    "id": "image_field",
                    "style": "height: 100px; width: 100px; border: 1px dashed #adb5bd; color: #adb5bd;",
                }
            ),
            "photo3": FileInput(
                attrs={
                    "id": "image_field",
                    "style": "height: 100px; width: 100px; border: 1px dashed #adb5bd; color: #adb5bd;",
                }
            ),
        }
