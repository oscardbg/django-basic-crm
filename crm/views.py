from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from crm.models import Customer, Order, Product
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from accounts.decorators import admin_only
from django.contrib import messages
from crm.forms import OrderForm

def home(request):
	return render(request, 'crm/index.html')

@login_required(login_url='accounts:login')
@admin_only
def dashboard(request):
	customers = Customer.objects.all()
	orders = Order.objects.all()
	pendingOrd = Order.objects.filter(status='Pending')
	delivOrd = Order.objects.filter(status='Delivered')

	context = { 
		'customers': customers,
		'orders': orders,
		'pendingOrd': pendingOrd,
		'delivOrd': delivOrd,
	}
	return render(request, 'crm/dashboard.html', context)

class ProductListView(ListView):
	model = Product

def user_page(request):
	return render(request, 'crm/user_page.html')

@login_required(login_url='accounts:login')
def customer(request, pk):
	customer = Customer.objects.get(id=pk)

	context = {
		'customer': customer
	}
	return render(request, 'crm/customer_detail.html', context)

@login_required(login_url='accounts:login')
def create_order(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=8)

	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
	#form = OrderForm(initial={'customer':customer})

	if request.method == 'POST':
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('crm:dashboard')

	context = {
		'formset': formset
	}
	return render(request, 'crm/order_form.html', context)

@login_required(login_url='accounts:login')
def update_order(request, pk):
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('crm:dashboard')

	context = {
		'order': order,
		'form': form
	}
	return render(request, 'crm/order_form.html', context)

@login_required(login_url='accounts:login')
def delete_order(request, pk):
	order = Order.objects.get(id=pk)

	if request.method == 'POST':
		order.delete()
		return redirect('crm:dashboard')

	context = {
		'order': order
	}
	return render(request, 'crm/order_delete.html', context)