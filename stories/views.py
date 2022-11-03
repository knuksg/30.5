from django.shortcuts import render, redirect, get_object_or_404
from .models import Story
from .forms import StoryForm


# Create your views here.
def index(request):
    stories = Story.objects.order_by("-pk")
    context = {
        "stories": stories,
    }
    return render(request, "stories/index.html", context)


def create(request):
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("stories:index")
    else:
        form = StoryForm()
    context = {"form": form}
    return render(request, "stories/create.html", context)


def detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    context = {
        "story": story,
    }
    return render(request, "stories/detail.html", context)


def update(request, pk):
    story = Story.objects.get(pk=pk)
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES, instance=story)
        if form.is_valid():
            form.save()
            return redirect("stories:detail", story.pk)
    else:
        form = StoryForm(instance=story)
    context = {"form": form}
    return render(request, "stories/update.html", context)


def delete(request, pk):
    story = Story.objects.get(pk=pk)
    story.delete()
    return redirect("stories:index")
