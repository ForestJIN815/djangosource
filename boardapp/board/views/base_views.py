from django.shortcuts import render, get_object_or_404
from ..models import Question, QuestionCount
from django.core.paginator import Paginator
from django.db.models import Q, Count
from tools.utils import get_client_ip, cnt  # (cnt 확인)


def detail(request, id):

    page = request.GET.get("page", 1)
    # 검색
    keyword = request.GET.get("keyword", "")
    # 정렬기준
    so = request.GET.get("so", "")

    question = get_object_or_404(Question, id=id)

    # 조회수
    ip = get_client_ip(request)
    # question 에 동일한 ip 가 있는지 확인
    QuestionCount.objects.filter(ip=ip, question=question).count()

    if cnt == 0:
        qc = QuestionCount(ip=ip, question=question)
        qc.save()
        if question.view_cnt:
            question.view_cnt += 1
        else:
            question.view_cnt = 1
        question.save()

    context = {
        "question": question,
        "page": page,
        "keyword": keyword,
        "so": so,
    }
    return render(request, "board/question_detail.html", context)


def index(request):

    # http://127.0.0.1:8000/board/?page=1&keyword=title
    page = request.GET.get("page", 1)
    # 검색
    keyword = request.GET.get("keyword", "")
    # 정렬기준
    so = request.GET.get("so", "")

    if so == "popular":
        objects = Question.objects.annotate(num_voter=Count("voter")).order_by(
            "-num_voter", "-created_at"
        )
    elif so == "recommend":
        objects = Question.objects.annotate(num_answer=Count("answer")).order_by(
            "-num_answer", "-created_at"
        )
    else:
        objects = Question.objects.order_by("-created_at")

    # 검색어가 제목 or 내용 or 질문작성자 or 답변작성자에 포함된 경우 추출
    # or : Q 사용
    if keyword:
        objects = objects.filter(
            Q(subject__icontains=keyword)
            | Q(content__icontains=keyword)
            | Q(author__username__icontains=keyword)
            | Q(answer__author__username__icontains=keyword)
        ).distinct()

    paginator = Paginator(objects, 10)
    question_list = paginator.get_page(page)

    context = {
        "question_list": question_list,
        "page": page,
        "keyword": keyword,
        "so": so,
    }
    return render(request, "board/question_list.html", context)
