# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Post/', views.Post, name = 'Post'),
    path('Home/', views.Home, name = 'Home'),
    path('', views.ViewPosts, name = 'ViewPosts'),

]