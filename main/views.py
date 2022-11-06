from django.shortcuts import render
from stories.models import Story
from restaurants.models import Restaurant, Tag
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    korea_restaurants = Tag.objects.filter(name="한식")
    china_restaurants = Tag.objects.filter(name="중식")
    japan_restaurants = Tag.objects.filter(name="일식")
    western_restaurants = Tag.objects.filter(name="양식")
    school_restaurants = Tag.objects.filter(name="분식")
    restaurants = sorted(Restaurant.objects.all(), key=lambda a: a.grade)
    stories = Story.objects.order_by("-pk")[:3]
    context = {
        "stories": stories,
        "restaurants": restaurants[::-1][:8],
        "korea_restaurants": korea_restaurants.count(),
        "china_restaurants": china_restaurants.count(),
        "japan_restaurants": japan_restaurants.count(),
        "western_restaurants": western_restaurants.count(),
        "school_restaurants": school_restaurants.count(),
    }
    return render(request, "main/index.html", context)


def search(request):
    page = request.GET.get("page", "1")  # 페이지
    kw = request.GET.get("kw", "")  # 검색어
    restaurant_list = Restaurant.objects.order_by("-created_at")
    tag = Tag.objects.filter(name__icontains=kw)
    if kw:
        restaurant_list = restaurant_list.filter(
            Q(name__icontains=kw)
            | Q(address__icontains=kw)  # 이름 검색
            | Q(tags__in=tag)  # 주소 검색  # 태그 검색
        ).distinct()

    paginator = Paginator(restaurant_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {"restaurant_list": page_obj, "page": page, "kw": kw}
    return render(request, "main/search.html", context)
