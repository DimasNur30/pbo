# urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('pengguna/', views.PenggunaUmumView.as_view(), name='pengguna_umum'),
    
    path('admin/', views.AdminView.as_view(), name='admin_dashboard'),
    path('statistik/', views.StatistikView.as_view(), name='statistik_harian'),
]
