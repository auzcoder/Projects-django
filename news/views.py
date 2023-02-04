from django.shortcuts import render
from django.views.generic import ListView
from .models import New


# Create your views here.
class PostListView(ListView):
    model = New
    template_name = 'news/news.html'
    context_object_name = 'news'