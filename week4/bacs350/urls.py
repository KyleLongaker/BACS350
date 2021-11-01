from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    #path('about', TemplateView.as_view(template_name="about.html")),
    #path('home', TemplateView.as_view(template_name="home.html")),
    # path('',include('Hello.urls')),
    #path('', TemplateView.as_view(template_name="home.html")),
    path ('admin/', admin.site.urls),
    path('', include('hero.urls')),
]