from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home_page_view(request):
	return render(request, 'website/layout.html')

def groupoA_page(request):
	return render(request, 'website/grupoA.html')

def groupoB_page(request):
	return render(request, 'website/grupoB.html')

def groupoC_page(request):
	return render(request, 'website/grupoC.html')