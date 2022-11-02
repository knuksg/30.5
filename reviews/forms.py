from .models import Review, ReviewImage
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["content", "rating"]
        labels = {
            "content": "리뷰 내용",
            "rating": "별점",
        }


class ReviewImageForm(forms.ModelForm):
    class Meta:
        model = ReviewImage
        fields = [
            "photo1",
            "photo2",
            "photo3",
        ]
