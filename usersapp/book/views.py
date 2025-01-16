from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm


def book_remove(request, id):
    # 모델 찾은 후 delete()
    book = get_object_or_404(Book, id=id)
    book.delete()
    # 목록으로 이동
    return redirect("books:list")


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("books:detail", id=book.id)
    else:
        form = BookForm()

    return render(request, "books/create.html", {"form": form})


def book_edit(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:detail", id=id)
    else:
        form = BookForm(instance=book)

    return render(request, "books/edit.html", {"form": form, "id": id})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "books/detail.html", {"book": book})


def book_list(request):
    book_list = Book.objects.order_by("-id")
    return render(request, "books/list.html", {"book_list": book_list})
