from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, "home.html")


def users_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})


# 비밀번호 초기화 view 생성
class CustomPasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset_form.html"
    success_url = reverse_lazy("password_reset_done")

    # 이메일이 있는지 확인 후 없으면 에러메세지 보여주기 / 이메일 존재 시 부모의
    # 폼 유효성 호출
    def form_valid(self, form):
        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            messages.info(self.request, "입력하신 이메일을 확인해 주세요")
            return redirect("password_reset")
