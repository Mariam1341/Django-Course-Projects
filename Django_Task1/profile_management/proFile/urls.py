from django.urls import path

from . import views

app_name = 'profile'
urlpatterns = [
     path('cv/', views.cv, name='cv'),
     path('friend_cv/', views.friend_cv,name = 'friend_cv'),
     path('', views.index, name = 'index'),

]