from django.shortcuts import render


def app1_list(request):
    return render(request, "app1/list.html")
