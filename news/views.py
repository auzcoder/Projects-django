from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import New, Category


# Create your views here.
class PostListView(ListView):
    model = New
    template_name = 'news/news.html'
    context_object_name = 'news'


class PostDetailView(DetailView):
    model = New
    template_name = 'news/news_detail.html'
    context_object_name = 'new'

class CategoryListView(ListView):
    model = Category
    template_name = 'news/news_detail.html'
    context_object_name = 'category'