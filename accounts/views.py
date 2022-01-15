from django.contrib.auth.forms import AuthenticationForm
from accounts.decorators import unauthenticated_user
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from accounts.forms import CreateUserForm
from django.contrib import messages

@unauthenticated_user
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

@unauthenticated_user
def login_page(request):
	form = AuthenticationForm()
	
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			messages.success(request, f'Welcome again {user} ')
			return redirect('crm:dashboard')
		else:
			messages.warning(request, 'Username or password incorrect')
	
	context = {
		'form': form
	}
	return render(request, 'accounts/login.html', context)

def logout_page(request):
	logout(request)
	messages.info(request, 'You have been logged out')
	return redirect('accounts:login')