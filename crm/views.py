from django.shortcuts import render

def home(request):
	return render(request, 'crm/index.html')

def dashboard(request):
	return render(request, 'crm/dashboard.html')