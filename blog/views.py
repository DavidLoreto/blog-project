from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render

from .models import BlogPost

#Class-based views
class HomePageView(ListView):
    template_name = 'home.html'
    model = BlogPost
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = BlogPost
    context_object_name = 'post'
    

class NewPostView(CreateView):
    model = BlogPost
    template_name = 'post_new.html'
    fields = "__all__"


class EditPostView(UpdateView):
    model = BlogPost
    template_name = 'post_edit.html'
    fields = ['title', 'content']


class DeletePostView(DeleteView):
    model = BlogPost
    template_name = 'post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('home')

#Functions views

