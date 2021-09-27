from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blogposts/", views.blog, name="blog_posts"),
    path("login_user/", views.login_user, name="login"),
    path('signup/', views.signup, name='signup'),
    path("logout_user/", views.logout_user, name='logout'),
]
