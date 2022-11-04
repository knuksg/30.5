from unicodedata import category
from django.shortcuts import render, redirect
from .models import Restaurant, Tag
from reviews.models import Review
from .forms import RestaurantsForm
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timedelta
from django.http import JsonResponse
from django.db.models import Q


def main(request):
    return render(request, "restaurants/main.html")

def index(request):
    print(request.POST)
    tags = request.POST.get("tag").replace(' ', '').split(',')
    print(tags)
    if len(tags) == 1:
        restaurants = Restaurant.objects.filter(tags__name=tags[0]).order_by("-pk")
    elif len(tags) == 2:
        restaurants = Restaurant.objects.filter(tags__name=tags[0]).filter(tags__name=tags[1]).order_by("-pk")
    context = {
        "restaurants": restaurants,
        "tag_name": tags,
    }
    return render(request, "restaurants/index.html", context)   


def korea(request):
    restaurants = Restaurant.objects.order_by("-pk")
    context = {
        "restaurants": restaurants,
    }
    return render(request, "restaurants/korea.html", context)


def china(request):
    restaurants = Restaurant.objects.order_by("-pk")
    context = {
        "restaurants": restaurants,
    }
    return render(request, "restaurants/china.html", context)


def japan(request):
    restaurants = Restaurant.objects.order_by("-pk")
    context = {
        "restaurants": restaurants,
    }
    return render(request, "restaurants/japan.html", context)


def western(request):
    restaurants = Restaurant.objects.order_by("-pk")
    context = {
        "restaurants": restaurants,
    }
    return render(request, "restaurants/western.html", context)


def school(request):
    restaurants = Restaurant.objects.order_by("-pk")
    context = {
        "restaurants": restaurants,
    }
    return render(request, "restaurants/school.html", context)


def category(request):
    return render(request, "restaurants/category.html")


def create(request):
    if request.method == "POST":
        restaurants_form = RestaurantsForm(request.POST, request.FILES)
        if restaurants_form.is_valid():
            new_restaurant = Restaurant(
                name=restaurants_form.cleaned_data["name"],
                address=restaurants_form.cleaned_data["address"],
                shop_number=restaurants_form.cleaned_data["shop_number"],
                between_pay=restaurants_form.cleaned_data["between_pay"],
                opening_time=restaurants_form.cleaned_data["opening_time"],
                break_day=restaurants_form.cleaned_data["break_day"],
            )
            new_restaurant.save()
            tags = restaurants_form.cleaned_data["tags"].split(",")
            for tag in tags:
                if not tag:
                    continue
                else:
                    tag = tag.strip()
                    _tag, _ = Tag.objects.get_or_create(name=tag)
                    new_restaurant.tags.add(_tag)
            return redirect("restaurants:main")
    else:
        restaurants_form = RestaurantsForm()
    context = {
        "restaurants_form": restaurants_form,
    }
    return render(request, "restaurants/create.html", context=context)


def detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    reviews = restaurant.review_set.all()
    reviews_count = len(reviews)
    likes = restaurant.like_users.all()

    ratings = []
    for review in reviews:
        ratings.append(review.rating)

    upper, middle, lower = 0, 0, 0
    for rating in ratings:
        if int(rating) > 3:
            upper += 1
        elif int(rating) == 3:
            middle += 1
        else:
            lower += 1

    context = {
        "restaurant": restaurant,
        "reviews": reviews[::-1],
        "upper": upper,
        "middle": middle,
        "lower": lower,
        "reviews_count": reviews_count,
        "likes": len(likes),
    }

    response = render(request, "restaurants/detail.html", context)

    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    cookie_value = request.COOKIES.get("hitboard", "_")

    if f"_{pk}_" not in cookie_value:
        cookie_value += f"_{pk}_"
        response.set_cookie(
            "hitboard", value=cookie_value, max_age=max_age, httponly=True
        )
        restaurant.hits += 1
        restaurant.save()

    return response


def update(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    if request.method == "POST":
        restaurants_form = RestaurantsForm(request.POST, request.FILES, instance=restaurant)
        if restaurants_form.is_valid():
            restaurant.tags.all().delete()
            tags = restaurants_form.cleaned_data["tags"].split(",")
            for tag in tags:
                if not tag:
                    continue
                else:
                    tag = tag.strip()
                    _tag, _ = Tag.objects.get_or_create(name=tag)
                    restaurant.tags.add(_tag)
            restaurants = restaurants_form.save(commit=False)
            restaurants.save()
            return redirect("restaurants:detail", pk)
    else:
        print(restaurant.tags.all())
        restaurants_form = RestaurantsForm(instance=restaurant)
        restaurants_form.tags = restaurant.tags.all()

    context = {
        "restaurants_form": restaurants_form,
    }
    return render(request, "restaurants/update.html", context=context)


def delete(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    restaurant.delete()
    return redirect("restaurants:main")


@login_required
def like(request, pk):
    print(request.POST)
    if request.user.is_authenticated:
        restaurant = Restaurant.objects.get(pk=pk)
        if restaurant.like_users.filter(pk=request.user.pk).exists():
            restaurant.like_users.remove(request.user)
            is_liked = False
        else:
            restaurant.like_users.add(request.user)
            is_liked = True
    else:
        return redirect("restaurants:detail", pk)
    return JsonResponse(
        {
            "is_liked": is_liked,
            "like_count": restaurant.like_users.count(),
        }
    )

    # if restaurant in request.user.like_restaurants.all():
    #     request.user.like_restaurants.remove(restaurant.pk)
    # else:
    #     request.user.like_restaurants.add(restaurant.pk)
    # return redirect("restaurants:detail", pk)
