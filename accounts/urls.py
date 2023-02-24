from django.urls import path
from accounts.views import user_login, AdminHomePageView, change_password
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('home/', AdminHomePageView.as_view(), name='admin_home_page'),
    path('login/', user_login, name='auth_login'),
    path('pass-change/', change_password, name='change_password'),
    path('pass-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]