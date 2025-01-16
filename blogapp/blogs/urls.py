from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    # http://127.0.0.1:8000/blogs
    path("", views.blogs_list, name="list")
]
