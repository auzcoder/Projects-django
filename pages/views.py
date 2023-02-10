from django.views.generic import TemplateView

from news.models import New, SubCategory, Category

class HomePageView(TemplateView):
    template_name = 'home.html'
