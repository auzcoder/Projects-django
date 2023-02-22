from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

import news
from .forms import LoginForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password']
                                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    success_url = 'admin_home_page'
                    return redirect(success_url)
                else:
                    return HttpResponse('Sizni hissobingiz faol holatda emas!')
            else:
                return HttpResponse('Login yoki parol xato!')

    else:
        return render(request, 'admin/login.html')

        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'admin/login.html', context)


class AdminHomePageView(ListView):
    model = User
    template_name = 'admin/home.html'
    context_object_name = 'admin_home_page'

