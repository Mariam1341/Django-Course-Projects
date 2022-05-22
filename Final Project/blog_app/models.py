from django.contrib.auth.models import User
from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length= 50)
    def __str__(self):
        return self.title

class Post(models.Model):
    tpic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    title = models.CharField(max_length= 50)
    descreption = models.CharField(max_length=100)
    content = models.TextField(max_length= 4000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    def __str__(self):
        return self.content[:10]
