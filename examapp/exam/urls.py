from django.urls import path, include
from .views import musician_create, musician_list, musician_edit
from .views import MusicianListView, MusicianDetailView, MusicianCreateView

urlpatterns = [
    # 클래스 뷰
    path("musician/list/", MusicianListView.as_view(), name="musician_list"),
    path("musician/<int:pk>/", MusicianDetailView.as_view(), name="musician_detail"),
    path("musician/create/", MusicianCreateView.as_view(), name="musician_create"),
    # 함수형 뷰 사용시
    # path("musician/list/", musician_list, name="musician_list"),
    path("musician/<int:id>/edit/", musician_edit, name="musician_edit"),
    # path("musician/create/", musician_create, name="musician_create"),
]
