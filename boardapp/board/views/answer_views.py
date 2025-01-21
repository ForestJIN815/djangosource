from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from board.models import Question, Answer
from board.forms import AnswerForm

from django.contrib.auth.decorators import login_required
from django.utils import timezone


################# 답변
@login_required(login_url="users:login")
def answer_modify(request, id):

    answer = get_object_or_404(Answer, id=id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modified_at = timezone.now()
            answer.save()
            # return redirect("board:detail", answer.question.id)
            # http://127.0.0.1:8000/board/question/300/#answer_5
            return redirect(
                "{}#answer_{}".format(
                    resolve_url("board:detail", answer.question.id), answer.id
                )
            )
    else:
        form = AnswerForm(instance=answer)
    return render(request, "board/answer_form.html", {"form": form})


@login_required(login_url="users:login")
def answer_delete(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer.delete()

    return redirect("board:detail", answer.question.id)


@login_required(login_url="users:login")
def answer_create(request, id):

    question = get_object_or_404(Question, id=id)

    # form 사용방식
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # form.save() Quetsion 정보 없음
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            # return redirect("board:detail", id)
            return redirect(
                "{}#answer_{}".format(resolve_url("board:detail", id), answer.id)
            )
    else:
        form = AnswerForm()

    # form 미 사용 방식
    # content = request.POST.get("content")

    # Answer 생성
    # 방법1)
    # answer = Answer(content=content, question=question)
    # answer.save()

    # 방법2)
    # Answer.objects.create(content=content, question=question)

    # 방법3)
    # question.answer_set.create(content=content)
    # return redirect("board:detail", id)

    context = {"form": form, "question": question}
    return render(request, "board/question_detail.html", context)
