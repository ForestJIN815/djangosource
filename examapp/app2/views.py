from django.shortcuts import render


def app2_list(request):
    return render(request, "app2/list.html")
