from crm.views import home, dashboard, ProductListView, customer, CustomerDetailView
from django.urls import path

app_name = 'crm'

urlpatterns = [
	path('', home, name='home'),
	path('dashboard/', dashboard, name='dashboard'),
	path('products/', ProductListView.as_view(), name='products'),
	path('customers/<int:pk>/', customer, name='customer')
]