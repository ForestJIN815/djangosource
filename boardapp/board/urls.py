from django.urls import path
from .views import index, detail, create, modify, delete, answer_create

app_name = "board"


urlpatterns = [
    # http://127.0.0.1:8000/board/
    path("", index, name="index"),
    # http://127.0.0.1:8000/board/question/1/
    path("question/<int:id>/", detail, name="detail"),
    # http://127.0.0.1:8000/board/question/create/
    path("question/create/", create, name="create"),
    # http://127.0.0.1:8000/board/question/modify/1/
    path("question/modify/<int:id>/", modify, name="modify"),
    # http://127.0.0.1:8000/board/question/delete/1/
    path("question/delete/<int:id>/", delete, name="delete"),
    ###### 답변
    # http://127.0.0.1:8000/board/answer/create/2/
    path("answer/create/<int:id>/", answer_create, name="answer_create"),
]
