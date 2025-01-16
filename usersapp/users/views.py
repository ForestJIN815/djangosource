from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm


def home(request):
    return render(request, "home.html")


def users_login(request):

    if request.method == "POST":
        # username,password 가져오기
        username = request.POST.get("username")
        password = request.POST.get("password")

        # db정보와 일치하다면 인증받은 객체 user 리턴
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # 세션에 user 정보 담기
            return redirect("users:home")

    return render(request, "users/login.html")


def users_logout(request):
    logout(request)
    return redirect("users:home")


def users_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
