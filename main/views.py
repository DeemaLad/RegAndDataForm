from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'main/index.html')

def vaccination(request):
	return render(request, 'main/vaccination.html')
