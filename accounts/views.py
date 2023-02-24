from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

from django.core.checks import messages
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




def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get("password_old")
        new_password = request.POST.get("password_new1")
        confirmed_new_password = request.POST.get("password_new2")

        if old_password and new_password and confirmed_new_password:
            if request.user.is_authenticated:
                user = User.objects.get(username=request.user.username)
                if not user.check_password(old_password):
                    messages.warning(request, "your old password is not correct!")
                else:
                    if new_password != confirmed_new_password:
                        messages.warning(request, "your new password not match the confirm password !")

                    elif len(new_password) < 8 or new_password.lower() == new_password or \
                            new_password.upper() == new_password or new_password.isalnum() or \
                            not any(i.isdigit() for i in new_password):
                        messages.warning(request, "your password is too weak!")



                    else:
                        user.set_password(new_password)
                        user.save()
                        update_session_auth_hash(request, user)

                        messages.success(request, "your password has been changed successfuly.!")

                        return redirect('dashboard_namespace:home')

        else:
            messages.warning(request, " sorry , all fields are required !")

    context = {

    }
    return render(request, "admin/reset-password.html", context)


i