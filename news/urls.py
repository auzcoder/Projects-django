from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import PostListView, PostDetailView

urlpatterns = [
    path('news/', PostListView.as_view(), name = 'post_list'),
    path('news/<int:id>/', PostDetailView.as_view(), name = 'post_detail'),
]


