"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls
from accounts import views

# 장고가 제공하는 login,logout,password reset, password change 사용하기
# 방법1) path("accounts/", include("django.contrib.auth.urls")),
#  로그인 시 기본 템플릿 경로는  registration/login.html 임 => 경로 페이지 맞춰서 페이지 작성
#  로그인 성공시 움직이는 경로 ~~~/profile/  ==> settings.py 에서 URL 변경 가능
#  로그아웃 성공시 움직이는 경로 ~~~/logout/  ==> settings.py 에서 URL 변경 가능

# 방법2) 프로젝트에 맞춰 수정하기

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    # path("accounts/", include("django.contrib.auth.urls")),
    # accounts/ login/ [name='login']
    # accounts/ logout/ [name='logout']
    # accounts/ password_change/ [name='password_change']
    # accounts/ password_change/done/ [name='password_change_done']
    # accounts/ password_reset/ [name='password_reset']
    # accounts/ password_reset/done/ [name='password_reset_done']
    # accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/ reset/done/ [name='password_reset_complete']
    path("accounts/", include("accounts.urls")),
]
