from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("", views.home, name="home"),
    # login,logout 직접 작성 시
    # path("login/", views.users_login, name="login"),
    # path("logout/", views.users_logout, name="logout"),
    # 장고의 auth 가 제공하는 login,loout class view 를 사용한다면
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.users_register, name="register"),
]
