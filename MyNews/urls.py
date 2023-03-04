
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from news.views import HomePageView, ContactPageView, NewsCreateView, NewsSearchView

urlpatterns = [
    path('auth/', include('accounts.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('', HomePageView, name='home'),
    path('news/', include('news.urls')),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('create/', NewsCreateView.as_view(), name='create_news'),
    path('search/', NewsSearchView.as_view(), name='search_news'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
