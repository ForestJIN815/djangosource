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
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import blogs_list
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs/", include("blogs.urls")),
    path("users/", include("users.urls")),
    # http://127.0.0.1:8000/ => http://127.0.0.1:8000/blogs/ 요청과 동일한 페이지 보여주기
    # 방법1) blogs 의 views 연결하기 : 요청주소 그대로 사용
    # path("", blogs_list, name="home"),
    # 방법2) RedirectView 사용하기 : 요청주소 => blogs list 주소로 변경
    path("", RedirectView.as_view(pattern_name="blogs:list")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
