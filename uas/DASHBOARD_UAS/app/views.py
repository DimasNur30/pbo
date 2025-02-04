# views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View



# Prinsip SRP: Setiap kelas memiliki tanggung jawab yang jelas

# View untuk pengguna umum
class PenggunaUmumView(View):
    def get(self, request):
        return HttpResponse('Hello, Pengguna Umum!')

# View untuk admin
class AdminView(View):
    def get(self, request):
        return HttpResponse('Welcome to the Admin Dashboard!')

# View untuk statistik umum
class StatistikView(View):
    def get(self, request):
        return HttpResponse('Statistik Harian')
