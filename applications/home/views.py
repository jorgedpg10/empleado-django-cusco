from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .models import Prueba
from .forms import PruebaForm

class IndexView(TemplateView):
    template_name = 'home/home.html' 


class PruebaCreateView(CreateView):
    template_name="home/add.html"
    model= Prueba
    form_class = PruebaForm
    success_url = '/'
