from django.shortcuts import render, redirect
from .models import restaurants, categorys
from .forms import restaurantsForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "restaurants/index.html")


def create(request):
    if request.method == 'POST':
        restaurants_form = restaurantsForm(request.POST, request.FILES)
        if restaurants_form.is_valid():
            restaurants = restaurants_form.save(commit=False)
            # 로그인한 유저 => 작성자네!
            # restaurants.user = request.user 
            restaurants.save()
            return redirect('restaurants:index')
    else: 
        restaurants_form = restaurantsForm()
    context = {
        'restaurants_form': restaurants_form
    }
    return render(request, 'restaurants/create.html', context=context)

def detail(request, pk):
    restaurant = restaurants.objects.get(pk=pk)
    context = {
        'restaurant': restaurant
    }
    return render(request, "restaurants/detail.html", context)

def update(request, pk):
    restaurant = restaurants.objects.get(pk=pk)
    # if request.user == restaurant.user: 
    if request.method == 'POST':
        # POST : input 값 가져와서, 검증하고, DB에 저장
        restaurant_form = restaurantsForm(request.POST, request.FILES, instance=restaurant)
        if restaurant_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            restaurant_form.save()
            # messages.success(request, '글이 수정되었습니다.')
            return redirect('restaurants:detail', restaurant.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 restaurant_form을 랜더링
    else:
        # GET : Form을 제공
        restaurant_form = restaurantsForm(instance=restaurant)
    context = {
        'restaurant_form': restaurant_form
    }
    return render(request, 'restaurants/update.html', context)
    # else:
    #     # 작성자가 아닐 때
    #     # (1) 403 에러메시지를 던져버린다. 
    #     # from django.http import HttpResponseForbidden
    #     # return HttpResponseForbidden()
    #     # (2) flash message 활용!
    #     return redirect('restaurants:detail', restaurant.pk)