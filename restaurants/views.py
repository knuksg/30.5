from unicodedata import category
from django.shortcuts import render, redirect
from .models import Restaurant, Category
from reviews.models import Review
from .forms import CategoryForm, RestaurantsForm
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, "restaurants/main.html")


def index(request):
    restaurants = Restaurant.objects.order_by("-pk")
    context = {"restaurants": restaurants}
    return render(request, "restaurants/index.html", context)


def category(request):
    return render(request, "restaurants/category.html")


def create(request):
    if request.method == "POST":
        restaurants_form = RestaurantsForm(request.POST, request.FILES)
        if restaurants_form.is_valid():
            restaurants = restaurants_form.save(commit=False)
            # 로그인한 유저 => 작성자네!
            # restaurants.user = request.user
            restaurants.save()
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
    context = {"restaurant": restaurant, "reviews": reviews}
    return render(request, "restaurants/detail.html", context)


def update(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    categroy = Category.objects.get(pk=pk)
    # if request.user == restaurant.user:
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        restaurant_form = RestaurantsForm(
            request.POST, request.FILES, instance=restaurant
        )
        category_form = CategoryForm(request.POST, request.FILES, instance=categroy)
        if restaurant_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            restaurant_form.save()
            # messages.success(request, '글이 수정되었습니다.')
            return redirect("restaurants:detail", restaurant.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 restaurant_form을 랜더링
    else:
        # GET : Form을 제공
        restaurant_form = RestaurantsForm(instance=restaurant)
        category_form = CategoryForm(instance=categroy)
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
