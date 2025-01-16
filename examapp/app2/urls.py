from django.urls import path
from . import views

app_name = "app2"

urlpatterns = [
    # http://127.0.0.1:8000/app2/
    path("", views.app2_list, name="list")
]
