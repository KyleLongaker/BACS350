from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . import models
# Create your views here.
class indexview(TemplateView):
    template_name ='index.html'

class heroListView(ListView):
    model = models.Hero
    template_name ='hero_lists.html'