from django.shortcuts import render
from .models import Post


def blogs_list(request):

    # 작성일자 내림차순
    post_list = Post.objects.order_by("-created_at")

    return render(request, "blogs/list.html", {"post_list": post_list})
