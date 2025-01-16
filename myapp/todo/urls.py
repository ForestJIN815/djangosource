from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/todo/
    path("", views.todo_list, name="todo_list"),
    # http://127.0.0.1:8000/todo/1 상세조회
    path("<int:id>/", views.todo_detail, name="todo_detail"),
    # http://127.0.0.1:8000/todo/new 할일등록
    path("new/", views.todo_register, name="todo_register"),
    # http://127.0.0.1:8000/todo/1/edit 할일수정
    path("<int:id>/edit/", views.todo_edit, name="todo_edit"),
    # http://127.0.0.1:8000/todo/done/ 완료된 목록 조회
    path("done/", views.todo_done, name="todo_done"),
]
