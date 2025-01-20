from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # 로그인 처리
            # username,password 가져오기
            # form.cleaned_data['username']
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            # db정보와 일치하다면 인증받은 객체 user 리턴
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # 세션에 user 정보 담기

            return redirect("board:index")
    else:
        form = UserForm()

    return render(request, "users/register.html", {"form": form})
