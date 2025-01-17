from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    # http://127.0.0.1:8000/blogs
    path("", views.blogs_list, name="list"),
    # http://127.0.0.1:8000/blogs/1/
    path("<int:pk>/", views.blogs_detail, name="detail"),
    # http://127.0.0.1:8000/create/
    path("create/", views.blogs_create, name="create"),
    # http://127.0.0.1:8000/blogs/1/update/
    path("<int:pk>/update", views.blogs_update, name="update"),
    # http://127.0.0.1:8000/blogs/1/delete/
    path("<int:pk>/delete", views.blogs_delete, name="delete"),
    # http://127.0.0.1:8000/blogs/1/comment/create/
    # path("<int:pk>/comment/create", views.comment_create, name="create"),
    path("<int:pk>/comment/create", views.comment_create, name="comment_create"),
    # http://127.0.0.1:8000/blogs/1/post/like/
    path("<int:pk>/post/like", views.post_like, name="post_like"),
]
