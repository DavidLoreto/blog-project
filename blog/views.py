from django.views.generic import ListView, DetailView
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
    

#Functions views

