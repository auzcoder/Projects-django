from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import PostListView

urlpatterns = [
    path('news/', PostListView.as_view(), name = 'post_list'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)