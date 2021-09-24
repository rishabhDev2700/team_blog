from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "base.html", {})


def blog(request):
    return render(request, "blogs.html", )


def login_user(request):
    return render(request, "blogs.html")
