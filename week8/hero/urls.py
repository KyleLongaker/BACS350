from django.urls import path
from . import views
urlpatterns =[
    path('', views.indexview.as_view(), name ='index'),
    path('hero/', views.heroListView.as_view(), name ='hero'),
    path('hero/<int:pk>', views.heroDetailView.as_view(), name='hero_detail'),
    path('hero/create', views.heroCreateView.as_view(), name ='Create'),
    path('hero/update/<int:pk>', views.heroUpdateView.as_view(), name ='Update'),
    path('hero/delete/<int:pk>', views.heroDeleteView.as_view(), name ='Delete'),
]