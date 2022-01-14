from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from accounts.forms import CreateUserForm
from django.contrib import messages
from django.shortcuts import render, redirect

def register_page(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, f'Account created. New user: {user} ')
			return redirect('crm:dashboard')

	context = {
		'form': form
	}
	return render(request, 'accounts/register.html', context)

def login_page(request):
	form = AuthenticationForm()
	
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			messages.success(request, f'Welcome again {user} ')
			return redirect('crm:dashboard')
	
	context = {
		'form': form
	}
	return render(request, 'accounts/login.html', context)

def logout_page(request):
	logout(request)
	return redirect('accounts:login')