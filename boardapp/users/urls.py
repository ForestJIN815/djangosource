from django.urls import path, reverse_lazy
from .views import register, CustomPasswordResetView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


app_name = "users"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # 비밀번호 변경(변경+세션에 있는 비밀번호 업데이트)
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="users/password_change.html",
            success_url=reverse_lazy("board:index"),
        ),
        name="password_change",
    ),
    # 비밀번호 초기화
    # 단계 1) 사용자에게 이메일 주소 입력받기
    path(
        "password_reset/",
        CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
