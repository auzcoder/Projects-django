from django.urls import path
from accounts.views import user_login, AdminHomePageView

urlpatterns = [
    path('home/', AdminHomePageView.as_view(), name='admin_home_page'),
    path('login/', user_login, name='auth_login')
]