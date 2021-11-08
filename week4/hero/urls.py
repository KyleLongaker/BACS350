from django.urls import path
from . import views
urlpatterns =[
    path('', views.indexview.as_view(), name ='index'),
    path('hero/', views.heroListView.as_view(), name ='hero'),
]