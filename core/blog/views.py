from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# Function Base Vieew show a template
'''
def indexView(request):
    """
    a funcion based view to show index page
    """
    context = {"name":"ali"}
    return render(request, "index.html",context)
'''

class IndexView(TemplateView):
    """
    a funcion based view to show index page
    """
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        context["name"] = "ali"
        return context
    
# Functhon Base View show a redirect
'''
def redirectToMaktab(request):
    return redirect('https://maktabkhooneh.com')
'''

class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    #queryset = Post.objects.all()
    context_object_name = 'posts' 
    paginate_by = 8
    ordering = "-id"
    #def get_queryset(self):
    #    posts = Post.objects.filter(status = True)
    #    return posts

class PostDetailView(DetailView):
    model = Post

'''
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/' 

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''

class PostCreateView(CreateView):
    model = Post
    #fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/post/'
    
    
    
    
