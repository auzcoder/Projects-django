from django import forms
from news.models import New

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AdminNewsUpdateView(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)


