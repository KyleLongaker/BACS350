from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from . import models
# Create your views here.
class indexview(TemplateView):
    template_name ='hero/index.html'

class heroListView(ListView):
    model = models.Hero
    template_name ='hero/hero_lists.html'

class heroDetailView (TemplateView):
    model =models.Hero
    template_name ="hero/hero_detail.html"

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero =models.Hero.objects.get(pk=hero_id)
        return {'hero' : hero}
class heroCreateView (CreateView):
    model = models.Hero
    fields = ['name', 'description']