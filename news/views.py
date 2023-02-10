from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import New, Category



examp = [
    {'id':1,"category_name":'Hududlar', 'sub':[{"id":22, 'name':'namangan'}]},
    {'id':1,"category_name":'Hududlar', 'sub':[{"id":22, 'name':'namangan'}]},
]

# Create your views here.
class PostListView(ListView):
    queryset = New.object.filter(status='PB')
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