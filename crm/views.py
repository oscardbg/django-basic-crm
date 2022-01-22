from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_only, allowed_users
from django.views.generic import ListView, DetailView
from crm.models import Customer, Order, Product
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from crm.forms import OrderForm, CustomerForm
from django.contrib import messages

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

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['customer'])
def user_page(request):
	customer = request.user.customer
	pendingOrd = Order.objects.filter(status='Pending')
	delivOrd = Order.objects.filter(status='Delivered')

	context = {
		'customer': customer,
		'pendingOrd': pendingOrd,
		'delivOrd': delivOrd
	}
	return render(request, 'crm/user_page.html', context)

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['customer'])
def account_settings(request):
	custmr = request.user.customer
	form = CustomerForm(instance=custmr)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES, instance=custmr)
		if form.is_valid():
			form.save()
		else:
			messages.warning(request, 'Some field data is incorrect')

	context = {
		'form': form
	}
	return render(request, 'crm/user_settings.html', context)

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
	customer = Customer.objects.get(id=pk)

	context = {
		'customer': customer
	}
	return render(request, 'crm/customer_detail.html', context)

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
def delete_order(request, pk):
	order = Order.objects.get(id=pk)

	if request.method == 'POST':
		order.delete()
		return redirect('crm:dashboard')

	context = {
		'order': order
	}
	return render(request, 'crm/order_delete.html', context)