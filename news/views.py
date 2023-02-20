from django.http import request, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

import news
from .models import New, Category
from django.views.generic import TemplateView
from .forms import ContactForm


# Class boyicha homepagega kategoriyalarni yangiliklarini chiqarish
# class HomePageView(ListView):
#     template_name = 'home.html'
#     news = New.object.all()
#     # category = Category.objects.all()
#     context_object_name = 'news'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         context['news_list'] = New.published.all().order_by('-date')[:9]
#         # [:9] bu listdan kelayotgan xabarlar sonini cheklash uchun hozir bu yerdan jami bo'lib 9 dona yangilik keladi
#         context['uzbekistan_news'] = New.published.all().filter(category__name='O\'zbekiston').order_by('-date')[0:3]
#         context['jahon_news'] = New.published.all().filter(category__name='Jahon').order_by('-date')[0:3]
#         context['iqtisod_news'] = New.published.all().filter(category__name='Iqtisodiyot').order_by('-date')[0:3]
#         context['jamiyat_news'] = New.published.all().filter(category__name='Jamiyat').order_by('-date')[0:3]
#         context['fantexnika_news'] = New.published.all().filter(category__name='Fan-texnika').order_by('-date')[0:3]
#         context['sport_news'] = New.published.all().filter(category__name='Sport').order_by('-date')[0:3]
#
#         return (context)

# Home page uchun yangiliklar views

def HomePageView(request):
    categories = Category.objects.all()
    news_list = New.published.all().order_by('-date')[:9] # [:9] bu listdan kelayotgan xabarlar sonini cheklash uchun hozir bu yerdan jami bo'lib 9 dona yangilik keladi
    uzbekistan_news = New.published.all().filter(category__name='O\'zbekiston').order_by('-date')[0:3]
    jahon_news = New.published.all().filter(category__name='Jahon').order_by('-date')[0:3]
    iqtisod_news = New.published.all().filter(category__name='Iqtisodiyot').order_by('-date')[0:3]
    jamiyat_news = New.published.all().filter(category__name='Jamiyat').order_by('-date')[0:3]
    fantexnika_news = New.published.all().filter(category__name='Fan-texnika').order_by('-date')[0:3]
    sport_news = New.published.all().filter(category__name='Sport').order_by('-date')[0:3]

    context = {
        'news_list': news_list,
        "categories": categories,
        'uzbekistan_news': uzbekistan_news,
        'jahon_news': jahon_news,
        'iqtisod_news': iqtisod_news,
        'jamiyat_news': jamiyat_news,
        'fantexnika_news': fantexnika_news,
        'sport_news': sport_news,
    }
    return render(request, 'home.html', context)

# Contact page uchun views
class ContactPageView(TemplateView):
    template_name = 'contact.html'
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }

        return render(request, 'contact.html', context)
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Bog'langaniz uchun tasahkkur!")

        context = {
            'form': form
        }

        return render(request, 'contact.html', context)



# examp = [
#     {'id':1,"category_name":'Hududlar', 'sub':[{"id":22, 'name':'namangan'}]},
#     {'id':1,"category_name":'Hududlar', 'sub':[{"id":22, 'name':'namangan'}]},
# ]

# Create your views here. Post listlar uchun
class PostListView(ListView):
    queryset = New.object.filter(status='PB', )
    template_name = 'news/news.html'
    context_object_name = 'news'


# Post detail uchun views
class PostDetailView(DetailView):
    model = New
    template_name = 'news/news_detail.html'
    context_object_name = 'news'



# Category uchun views
class CategoryListView(ListView):
    model = Category
    template_name = 'news/news_detail.html'
    context_object_name = 'category'


class NewsUpdateView(UpdateView):
    model = New
    fields = ('name', 'description', 'full_info', 'header_images', 'category', 'sub_category', 'status')
    template_name = 'news/edit/update.html'
    success_url = reverse_lazy('home')

class NewsDeleteView(DeleteView):
    model = New
    template_name = 'news/edit/delete.html'
    success_url = reverse_lazy('home')

class NewsCreateView(CreateView):
    model = New
    fields = ('name', 'description', 'full_info', 'header_images', 'category', 'sub_category', 'status')
    template_name = 'news/edit/create.html'
    success_url = reverse_lazy('post_list')