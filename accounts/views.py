from django.shortcuts import render
from django.views.generic import TemplateView
from .import forms
from django.views.generic import CreateView
from django.urls import reverse_lazy #if someone logged in/out
# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'


class SignUp(CreateView):
    form_class = forms.MainUser
    success_url = reverse_lazy('login')#if managed to log in go to login
    template_name = 'accounts/signup.html' #which template to show


