from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    amount_of_upvotes = models.IntegerField()


class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now=True)
