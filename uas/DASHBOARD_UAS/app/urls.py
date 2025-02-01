from django.urls import path
from . import views

urlpatterns = [
  path('', views.dashboard1, name='dashboard1'),
  path('statistik_harian/', views.statistik_harian, name='statistik_harian'),
]