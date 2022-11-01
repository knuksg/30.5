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