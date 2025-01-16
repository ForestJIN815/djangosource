from django.urls import path
from . import views

# from .views import book_list

app_name = "books"

urlpatterns = [
    # http://127.0.0.1:8000/books/ 전체도서목록(list)
    path("", views.book_list, name="list"),
    # http://127.0.0.1:8000/books/1/ 도서조회(detail)
    path("<int:id>/", views.book_detail, name="detail"),
    # http://127.0.0.1:8000/books/1/edit/ 도서수정(edit)
    path("<int:id>/edit/", views.book_edit, name="edit"),
    # http://127.0.0.1:8000/books/1/remove/ 도서삭제(remove)
    path("<int:id>/remove/", views.book_remove, name="remove"),
    # http://127.0.0.1:8000/books/create/ 도서추가(create)
    path("create/", views.book_create, name="create"),
]
