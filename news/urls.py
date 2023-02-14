from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name = 'post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
]

