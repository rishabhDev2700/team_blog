from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .models import BlogPost, Author


def home(request):
    user = request.user
    print(user.username)
    user = User.objects.get(username='rishi')
    print(user.last_name)
    return render(request, "base.html", {})


def blog(request):
    # if request.method == 'POST':
    # author = request.user.
    # title = request.POST['blog_title']
    # content = request.POST['blog_content']
    # blogpost = BlogPost(author=,title=title,content=content)
    # blogpost.save()

    return render(request, "blogs.html", )


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is None:
                return render(request, 'login.html')
            login(request, user)
            return redirect('home')

    form = LoginForm()
    return render(request, "login.html", {'form': form})


def signup(request):
    if request.method == 'POST':
        fname = request.POST['first-name']
        lname = request.POST['last-name']
        email = request.POST['email']
        username = request.POST['user-username']
        dob = request.POST['DOB']
        password = request.POST['user-password']
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()
        Author(user=new_user, date_of_birth=dob).save()
        messages.success(request, "Account Created successfully")
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('home')
