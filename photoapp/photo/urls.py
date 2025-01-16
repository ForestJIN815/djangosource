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

from django.urls import path
from .views import photo_list, photo_edit, photo_detail, photo_post, photo_remove

urlpatterns = [
    # http://127.0.0.1:8000/photo/
    path("", photo_list, name="photo_list"),
    # http://127.0.0.1:8000/photo/1/ 상세조회
    path("<int:id>/", photo_detail, name="photo_detail"),
    # http://127.0.0.1:8000/photo/1/edit/ 수정
    path("<int:id>/edit/", photo_edit, name="photo_edit"),
    # http://127.0.0.1:8000/photo/new/ 추가
    path("new/", photo_post, name="photo_post"),
    # http://127.0.0.1:8000/photo/1/remove/ 삭제
    path("<int:id>/remove/", photo_remove, name="photo_remove"),
]
