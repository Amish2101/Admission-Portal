from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'base/base.html'

class Login(TemplateView):
    template_name = 'base/signin.html'