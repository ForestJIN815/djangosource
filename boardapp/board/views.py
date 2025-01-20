from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils import timezone


################# 답변
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
            return redirect("board:detail", id)
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


################# 질문
def delete(request, id):
    question = get_object_or_404(Question, id=id)
    question.delete()
    return redirect("board:index")


def modify(request, id):

    question = get_object_or_404(Question, id=id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modified_at = timezone.now()
            question.save()
            return redirect("board:detail", id)
    else:
        form = QuestionForm(instance=question)
    return render(request, "board/question_form.html", {"form": form})


@login_required(login_url="users:login")
def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect("board:index")
    else:
        form = QuestionForm()
    return render(request, "board/question_form.html", {"form": form})


def detail(request, id):
    question = get_object_or_404(Question, id=id)
    return render(request, "board/question_detail.html", {"question": question})


def index(request):

    # http://127.0.0.1:8000/board/?page=1
    page = request.GET.get("page", 1)

    # 전체 질문 추출(작성일시 내림차순)
    objects = Question.objects.order_by("-created_at")

    paginator = Paginator(objects, 10)
    question_list = paginator.get_page(page)

    return render(request, "board/question_list.html", {"question_list": question_list})
