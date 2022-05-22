from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import  ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

def home(request):
     return render(request, 'blog/home.html')


class PostsListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    context_object_name='post'
    ordering = ['-created_at']
    template_name='blog/post_details.html'



class PostCreateView(CreateView):
    model = Post
    fields = ('tpic','title','descreption','content')
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('blog_app:post_list')



class PostUpdateView(UpdateView):
    model = Post
    fields = ('content',)
    template_name_suffix = '_post'
    template_name = 'blog/update_post.html'
    success_url = reverse_lazy('blog_app:post_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog_app:post_list')
    template_name_suffix = '_delete'




class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('blog_app:login')
    template_name = 'blog/signup.html'

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('usernsme')
#             password =  form.cleaned_data.get('password1')
#             user = authenticate(username= username,password = password)
#             login(request,user)
#             return redirect('/home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'blog/signup.html', {'form': form})














