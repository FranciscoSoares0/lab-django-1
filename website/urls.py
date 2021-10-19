from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('layout', views.home_page_view, name='layout'),
    path('grupoA', views.groupoA_page, name='grupoA'),
    path('grupoB', views.groupoB_page, name='grupoB'),
    path('grupoC', views.groupoC_page, name='grupoC')
]