from django.urls import path

# from . import views
from .views import app1_list

app_name = "app1"

urlpatterns = [
    # http://127.0.0.1:8000/app1
    # path("", views.app1_list, name="list")
    path("", app1_list, name="list")
]
