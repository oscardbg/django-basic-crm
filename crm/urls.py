from crm.views import home
from django.urls import path

app_name = 'crm'

urlpatterns = [
	path('', home, name='home')
]