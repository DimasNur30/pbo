from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
class PenggunaUmumView(View):
    def get(self, request):
        return HttpResponse('Hello, Pengguna Umum!')

class AdminView(View):
    def get(self, request):
        return HttpResponse('Welcome to the Admin Dashboard!')

class StatistikView(View):
    def get(self, request):
        return HttpResponse('Statistik Harian')
