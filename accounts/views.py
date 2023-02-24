from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash, user_logged_out

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
                    return HttpResponse(request, "Eski parolingiz noto'g'ri!")
                else:
                    if new_password != confirmed_new_password:
                        return HttpResponse(request, "Yangi parolingiz tasdiqlash paroliga mos kelmaydi!")

                    elif len(new_password) < 5 or  \
                            not any(i.isdigit() for i in new_password):
                        return HttpResponse("Parolingiz juda zaif!")

                    else:
                        user.set_password(new_password)
                        user.save()
                        update_session_auth_hash(request, user)

                        return HttpResponse(request, "Parolingiz muvaffaqiyatli o'zgartirildi!")

                        return redirect('admin_home_page')

        else:
            return HttpResponse(request, " Kechirasiz, barcha maydonlarni to'ldirish shart!")

    context = {

    }
    return render(request, "admin/reset-password.html", context)



def logout(request):
    """
    Removes the authenticated user's ID from the request and flushes their
    session data.
    """
    # Dispatch the signal before the user is logged out so the receivers have a
    # chance to find out *who* logged out.
    user = getattr(request, 'user', None)
    if hasattr(user, 'is_authenticated') and not user.is_authenticated():
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)

    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()

