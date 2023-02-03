from django.urls import path

from .views import PostListView

urlpatterns = [
    path('news/', PostListView.as_view(), name = 'post_list'),
]