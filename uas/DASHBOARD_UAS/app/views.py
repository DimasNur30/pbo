from django.shortcuts import render

# Create your views here.
def dashboard1(request):
  return render(request, 'dashboard1.html')

def statistik_harian(request):
  return render(request, 'statistik_harian.html')