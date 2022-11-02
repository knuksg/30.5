from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from restaurants.models import Restaurant
from django.http import JsonResponse
from .forms import ReviewForm
from .models import Review


def index(request):
    contents = Review.objects.all()
    context = {"review": contents}
    return render(request, "reviews/index.html", context)


@login_required
def review_create(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(review=False)
        review.restaurant = restaurant
        review.user = request.user
        review.save()
        context = {
            "content": review.content,
            "userName": review.user.username,
        }
        return JsonResponse(context)
