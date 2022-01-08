from django.shortcuts import render
from crm.models import Customer, Order, Product

def home(request):
	return render(request, 'crm/index.html')

def dashboard(request):
	customers = Customer.objects.all()
	orders = Order.objects.all()
	products = Product.objects.all()

	context = { 
		'customers': customers,
		'orders': orders,
		'products': products
	}
	return render(request, 'crm/dashboard.html', context)