from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'blog_app'

urlpatterns = [
    path('',views.home, name = 'home'),

    path('signup/',views.SignUpView.as_view(), name='signup'),

    path('post_list/', views.PostsListView.as_view(), name = 'post_list'),

    path('post_details/<pk>/', views.PostDetailView.as_view(), name='post_details'),

    path('create_post/', views.PostCreateView.as_view(), name='create_post'),

    path('update_post/<pk>', views.PostUpdateView.as_view(), name='update_post'),

    path('delete_post/<pk>/', views.PostDeleteView.as_view(), name='post_delete'),

    path('login/', LoginView.as_view(template_name='blog/login.html', success_url= 'blog/post_list.html' ), name='login'),

    path('logout/', LogoutView.as_view(template_name='blog_app/logout.html'), name='logout'),



]