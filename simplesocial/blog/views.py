from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from blog.models import BlogPost, BlogComment
from blog.forms import BlogPostForm,BlogCommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView,ListView,
DetailView,CreateView,
UpdateView,DeleteView)

# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    redirect_field_name = 'blog:post_list'
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
class PostDetailView(DetailView):
    model = BlogPost

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/'
    redirect_field_name = 'blog:post_detail'
    form_class = BlogPostForm
    model = BlogPost

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView,self).form_valid(form)


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/'
    redirect_field_name = 'blog:post_detail'
    form_class = BlogPostForm
    model = BlogPost

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:post_list')

class DraftPostView(LoginRequiredMixin,ListView):    
    login_url = '/'
    redirect_field_name = 'blog/blog_post_draft_list.html'
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__isnull=True).order_by('created_date')       
        
##################################
######## FUNCTION VIEWS ##########       
##################################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=post.pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    if request.method == "POST":
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = BlogCommentForm()
    return render(request,'blog/blog_comment_form.html',{'form':form})    

@login_required
def approve_comment(request,pk):
    comment = get_object_or_404(BlogComment,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def remove_comment(request,pk):
    comment = get_object_or_404(BlogComment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)

