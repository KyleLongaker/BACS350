from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView

urlpatterns = [
    path('about', TemplateView.as_view(template_name="about.html")),
    path('home', TemplateView.as_view(template_name="home.html")),
    path('',include('Hello.urls')),
]