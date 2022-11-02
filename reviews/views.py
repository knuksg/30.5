import re
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from restaurants.models import Restaurant
from django.http import JsonResponse
from .forms import ReviewForm, ReviewImageForm
from .models import Review


def index(request):
    contents = Review.objects.all()  # Restaurant
    context = {
        "review": contents,
    }
    return render(request, "reviews/index.html", context)


@login_required
def review_create(request, pk):
    if request.method == "POST":
        restaurant = get_object_or_404(Restaurant, pk=pk)
        review_form = ReviewForm(request.POST)
        reviewimage_form = ReviewImageForm(request.POST, request.FILES)
        if review_form.is_valid():
            # 리뷰내용 폼
            review = review_form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()
            # 리뷰 이미지 폼
            review_image = reviewimage_form.save(commit=False)
            review_image.restaurant = restaurant
            review_image.reviews = review
            review_image.user = request.user
            review_image.save()
            return redirect("restaurants:detail", pk)
    else:
        review_form = ReviewForm()
        reviewimage_form = ReviewImageForm()
    context = {
        # "content": review.content,
        # "userName": review.user.username,
        "review_form": review_form,
        "reviewimage_form": reviewimage_form,
    }
    return render(request, "reviews/review_create.html", context)


def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        "context": context,
    }
    return render(request, "review_detail.html", context)
