from django.urls import path
from . import views


urlpatterns = [
    path('pengguna_umum/', views.PenggunaUmumView.as_view(), name='pengguna_umum.html/'),
    path('admin_dashboard/', views.AdminView.as_view(), name='admin_dashboard.html'),
    path('statistik/', views.StatistikView.as_view(), name='statistik_harian.html'),

]
