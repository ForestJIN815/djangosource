from django.shortcuts import render, redirect
from .forms import UserForm


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user 의 gender 요소가 비어있는지 확인
            if form.cleaned_data["gender"] == "":
                user.gender = 2
            user.save()
            return redirect("blogs:list")
    else:
        form = UserForm()
    return render(request, "users/register.html", {"form": form})
