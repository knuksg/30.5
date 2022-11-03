from django.shortcuts import render, redirect, get_object_or_404
from .models import Story
from .forms import StoryForm
from restaurants.models import Restaurant
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    stories = Story.objects.order_by('-pk')
    context = {
        'stories': stories,
    }
    return render(request, 'stories/index.html', context)

def create(request):
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('stories:index')
    else:
        form = StoryForm()
    context = {
        'form':form
    }
    return render(request, 'stories/create.html', context)

def detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    context = {
        'story': story,
    }
    return render(request, 'stories/detail.html', context)

def update(request, pk):
    story = Story.objects.get(pk=pk)
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES, instance=story)
        if form.is_valid():
            form.save()
            return redirect('stories:detail', story.pk)
    else:
        form = StoryForm(instance=story)
    context = {
        'form': form
    }
    return render(request, 'stories/update.html', context)

def search_test(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    restaurant_list = Restaurant.objects.order_by('-created_at')
    if kw:
        restaurant_list = restaurant_list.filter(
            Q(name__icontains=kw) |  # 이름 검색
            Q(address__icontains=kw)  # 주소 검색
        ).distinct()
    paginator = Paginator(restaurant_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'restaurant_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'stories/search_test.html', context)  