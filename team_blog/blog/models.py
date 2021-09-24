from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()


class BlogPost(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
