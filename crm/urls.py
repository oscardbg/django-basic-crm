from crm.views import home, dashboard
from django.urls import path

app_name = 'crm'

urlpatterns = [
	path('', home, name='home'),
	path('dashboard', dashboard, name='dashboard'),
]