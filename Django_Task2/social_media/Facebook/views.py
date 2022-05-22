from django.shortcuts import render
from .models import Post
# Create your views here.

def creatPost(request):
    return render(request,'Facebook/Post.html')

def ViewPosts(request):
    return render(request,'Facebook/ViewPosts.html',{'posts_list' : Post.objects.all()})

def Home(request):
    return render(request,'Facebook/Home.html')