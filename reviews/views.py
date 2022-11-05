from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from restaurants.models import Restaurant
from django.contrib import messages
from .forms import ReviewForm, ReviewImageForm
from .models import Review, ReviewImage


def index(request):
    contents = Review.objects.all()  # Restaurant
    context = {
        "review": contents,
    }
    return render(request, "reviews/index.html", context)


@login_required
def review_create(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
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
        "review_form": review_form,
        "reviewimage_form": reviewimage_form,
        "restaurant": restaurant,
    }
    return render(request, "reviews/review_create.html", context)


def review_detail(request, restaurant_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    reviewimage = ReviewImage.objects.get(pk=review_pk)
    restaurant = get_object_or_404(Restaurant, pk=restaurant_pk)
    context = {
        "review": review,
        "restaurant": restaurant,
        "reviewimage": reviewimage,
    }
    return render(request, "reviews/review_detail.html", context)


def review_delete(request, restaurant_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    restaurant = get_object_or_404(Restaurant, pk=restaurant_pk)
    if request.user == review.user:
        review = Review.objects.get(pk=review_pk)
        review.delete()
        return redirect("restaurants:detail", restaurant_pk)
    else:
        messages.warning(request, "권한 없음.")
        context = {"review": review}
        return render(
            request, "reviews/review_detail.html", context, review.pk, restaurant_pk
        )


def review_update(request, review_pk, restaurant_pk):
    review = get_object_or_404(Review, pk=review_pk)
    restaurant = get_object_or_404(Restaurant, pk=restaurant_pk)
    reviewimage = get_object_or_404(ReviewImage, pk=review_pk)
    if request.user == review.user:
        if request.method == "POST":
            review_form = ReviewForm(request.POST, instance=review)
            reviewimage_form = ReviewImageForm(
                request.POST, request.FILES, instance=reviewimage
            )
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
                messages.success(request, "글이 수정되었습니다.")
                return redirect("reviews:review_detail", restaurant_pk, review_pk)
        else:
            review_form = ReviewForm(instance=review)
            reviewimage_form = ReviewImageForm(instance=reviewimage)
        context = {
            "review_form": review_form,
            "reviewimage_form": reviewimage_form,
            "restaurant": restaurant,
        }
        return render(request, "reviews/review_update.html", context)
