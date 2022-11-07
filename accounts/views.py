from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
    CustomAuthenticationForm,
)
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def index(request):
    users = get_user_model().objects.all()
    context = {"users": users}
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("main:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    context = {
        "user": user,
        "my": request.user,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("main:index")


def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "main:index")
    else:
        form = CustomAuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("main:index")


@login_required
def follow(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    if user != request.user:
        if user.followings.filter(pk=request.user.pk).exists():
            user.followings.remove(request.user)
            # 팔로우 여부를 확인할 변수 생성💡
            is_followed = False
        else:
            user.followings.add(request.user)
            # 팔로우 여부를 확인할 변수 생성💡
            is_followed = True
        # json response💡
        return JsonResponse(
            {
                "is_followed": is_followed,
                "followers_count": user.followings.count(),
                "followings_count": user.followers.count(),
            }
        )
    return redirect("accounts:detail", user_pk)
