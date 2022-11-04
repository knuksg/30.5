from unicodedata import category
from django.shortcuts import render, redirect
from .models import Restaurant, Tag
from reviews.models import Review
from .forms import RestaurantsForm, TagForm
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timedelta
from django.http import JsonResponse


def main(request):
    return render(request, "restaurants/main.html")


def index(request):
    restaurants = Restaurant.objects.order_by("-pk")
    context = {
        "restaurants": restaurants,
    }
    return render(request, "restaurants/index.html", context)


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
        tag_form = TagForm()
    context = {
        "restaurants_form": restaurants_form,
        "tag_form": tag_form,
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
    category = Category.objects.get(restaurant_id=restaurant)
    # if request.user == restaurant.user:
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        restaurant_form = RestaurantsForm(
            request.POST, request.FILES, instance=restaurant
        )
        category_form = CategoryForm(request.POST, request.FILES, instance=category)
        if restaurant_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            restaurants = restaurant_form.save(commit=False)
            restaurants.save()
            categorys = category_form.save(commit=False)
            categorys.save()
            # messages.success(request, '글이 수정되었습니다.')
            return redirect("restaurants:detail", pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 restaurant_form을 랜더링
    else:
        # GET : Form을 제공
        restaurant_form = RestaurantsForm(instance=restaurant)
        category_form = CategoryForm(instance=category)
    context = {
        "restaurant_form": restaurant_form,
        "category_form": category_form,
    }
    return render(request, "restaurants/update.html", context)
    # else:
    #     # 작성자가 아닐 때
    #     # (1) 403 에러메시지를 던져버린다.
    #     # from django.http import HttpResponseForbidden
    #     # return HttpResponseForbidden()
    #     # (2) flash message 활용!
    #     return redirect('restaurants:detail', restaurant.pk)


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
