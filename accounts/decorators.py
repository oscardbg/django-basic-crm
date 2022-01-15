from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_funct):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('crm:dashboard')
		else:
			return view_funct(request, *args, **kwargs)
	
	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_funct):
		def wrapper_funct(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			
			if group in allowed_roles:
				return view_funct(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized')
		
		return wrapper_funct
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'customer':
			return redirect('crm:userpage')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function