from django.shortcuts import render, get_object_or_404, redirect
from board.models import Question, Answer, Comment
from board.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


################# 댓글
@login_required(login_url="users:login")
def comment_create_question(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.question = question
            comment.save()
            return redirect("board:detail", comment.question.id)
    else:
        form = CommentForm()
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="users:login")
def comment_modify_question(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            return redirect("board:detail", comment.question.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="users:login")
def comment_delete_question(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect("board:detail", comment.question.id)


@login_required(login_url="users:login")
def comment_create_answer(request, id):
    answer = get_object_or_404(Answer, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.answer = answer
            comment.save()
            return redirect("board:detail", comment.answer.question.id)
    else:
        form = CommentForm()
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="users:login")
def comment_modify_answer(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            return redirect("board:detail", comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="users:login")
def comment_delete_answer(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect("board:detail", comment.answer.question.id)
