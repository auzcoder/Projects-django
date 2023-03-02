from django.urls import path
from .views import PostListView, PostDetailView, NewsUpdateView, NewsDeleteView, NewsSearchView

# urls

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', NewsUpdateView.as_view(), name='post_edit'),
    path('delete/<slug:slug>/', NewsDeleteView.as_view(), name='post_delete'),
    path('search/', NewsSearchView.as_view(), name='search_news'),
]