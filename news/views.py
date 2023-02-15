from django.http import request, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import New, Category
from django.views.generic import TemplateView
from .forms import ContactForm

# class HomePageView(TemplateView):
#     template_name = 'home.html'
#     news = New.object.all()
#     category = Category.objects.all()
#     context_object_name = 'home_page_news'

def HomePageView(request):
    categories = Category.objects.all()
    news_list = New.published.all().order_by('-date')[:9] # [:9] bu listdan kelayotgan xabarlar sonini cheklash uchun hozir bu yerdan jami bo'lib 9 dona yangilik keladi
    uzbekistan_news = New.published.all().filter(category__name='O\'zbekiston')
    jahon_news = New.published.all().filter(category__name='Jahon')
    iqtisod_news = New.published.all().filter(category__name='Iqtisodiyot')
    jamiyat_news = New.published.all().filter(category__name='Jamiyat')
    fantexnika_news = New.published.all().filter(category__name='Fan-texnika')
    sport_news = New.published.all().filter(category__name='Sport')

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

class ContactPageView(TemplateView):
    template_name = 'contact.html'
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form':form
        }

        return render(request, 'contact.html', context)
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Bog'langaniz uchun tasahkkur!")

        context = {
            'form':form
        }

        return render(request, 'contact.html', context)



# examp = [
#     {'id':1,"category_name":'Hududlar', 'sub':[{"id":22, 'name':'namangan'}]},
#     {'id':1,"category_name":'Hududlar', 'sub':[{"id":22, 'name':'namangan'}]},
# ]

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

