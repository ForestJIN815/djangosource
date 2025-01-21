from django.urls import path
from .views.base_views import index, detail
from .views.question_views import create, modify, delete
from .views.answer_views import answer_create, answer_modify, answer_delete
from .views.comment_views import (
    comment_create_answer,
    comment_modify_answer,
    comment_delete_answer,
    comment_create_question,
    comment_modify_question,
    comment_delete_question,
)
from .views.vote_views import vote_question, vote_answer


app_name = "board"

urlpatterns = [
    # 추천
    # http://127.0.0.1:8000/board/question/vote/<int:question_id>/
    path("question/vote/<int:question_id>/", vote_question, name="vote_question"),
    # http://127.0.0.1:8000/board/answer/vote/<int:answer_id>/
    path("answer/vote/<int:answer_id>/", vote_answer, name="vote_answer"),
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
    # http://127.0.0.1:8000/board/answer/modify/2/
    path("answer/modify/<int:id>/", answer_modify, name="answer_modify"),
    # http://127.0.0.1:8000/board/answer/modify/2/
    path("answer/delete/<int:id>/", answer_delete, name="answer_delete"),
    ###### 댓글
    # http://127.0.0.1:8000/board/comment/create/question/ 질문댓글추가
    path(
        "comment/create/question/<int:id>/",
        comment_create_question,
        name="comment_create_question",
    ),
    # http://127.0.0.1:8000/board/comment/modify/question/1/ 질문댓글수정
    path(
        "comment/modify/question/<int:id>/",
        comment_modify_question,
        name="comment_modify_question",
    ),
    # http://127.0.0.1:8000/board/comment/delete/question/1/ 질문댓글삭제
    path(
        "comment/delete/question/<int:id>/",
        comment_delete_question,
        name="comment_delete_question",
    ),
    # http://127.0.0.1:8000/board/comment/create/answer/1/ 답변댓글추가
    path(
        "comment/create/answer/<int:id>/",
        comment_create_answer,
        name="comment_create_answer",
    ),
    # http://127.0.0.1:8000/board/comment/modify/answer/1/ 답변댓글수정
    path(
        "comment/modify/answer/<int:id>/",
        comment_modify_answer,
        name="comment_modify_answer",
    ),
    # http://127.0.0.1:8000/board/comment/delete/answer/1/ 답변댓글삭제
    path(
        "comment/delete/answer/<int:id>/",
        comment_delete_answer,
        name="comment_delete_answer",
    ),
]
