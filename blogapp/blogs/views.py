from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator

# @login_required : 로그인이 안 되어 있을 때 로그인 페이지로 이동


@login_required
def post_like(request, pk):

    post = get_object_or_404(Post, pk=pk)
    is_liked = post.likes.filter(id=request.user.id).exists()
    if is_liked:
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    return JsonResponse({"likes_count": post.likes.count(), "is_liked": is_liked})


################################################### HttpResponse ###################################################


@login_required(login_url="users:login")
def comment_create(request):
    if request.method == "POST":
        content = request.POST.get("content").strip()
        post_pk = request.POST.get("post_pk").strip()

        post = get_object_or_404(Post, pk=post_pk)

        if content and post_pk:
            # Comment 생성
            # comment = Comment(post=post, user=request.user, content=content)
            # comment.save()
            comment = Comment.objects.create(
                post=post, user=request.user, content=content
            )
            return redirect("blogs:detail", pk=comment.post.pk)

    messages.error(request, "댓글을 입력해 주세요")
    return redirect("blogs:detail", pk=post_pk)


@login_required
def blogs_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("blogs:list")


@login_required
def blogs_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blogs:detail", pk=pk)
    else:
        form = PostForm(instance=post)

    return render(request, "blogs/update.html", {"form": form, "pk": pk})


def blogs_create(request):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # 작성자(== 로그인 사용자)
            post.user = request.user
            post.save()
            # 태그 저장
            form.save_m2m()
            return redirect("blogs:list")
    else:
        form = PostForm()

    return render(request, "blogs/create.html", {"form": form})


def blogs_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 현재 로그인한 유저가 게시물에 좋아요를 누른 상태 확인
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    return render(request, "blogs/detail.html", {"post": post, "is_liked": is_liked})


def blogs_list(request):

    # 페이지번호 가져오기
    # request.POST.get()
    page = request.GET.get("page", 1)

    # 작성일자 내림차순
    posts = Post.objects.order_by("-created_at")

    paginator = Paginator(posts, 10)
    post_list = paginator.get_page(page)

    return render(request, "blogs/list.html", {"post_list": post_list})
