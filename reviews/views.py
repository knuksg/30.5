from django.shortcuts import render


def index(request):
    return render(request, "reviews/index.html")

def review_create(request):
    pass
