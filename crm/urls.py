from crm.views import delete_order, home, dashboard, ProductListView, customer, create_order, update_order, delete_order
from django.urls import path

app_name = 'crm'

urlpatterns = [
	path('', home, name='home'),
	path('dashboard/', dashboard, name='dashboard'),
	path('products/', ProductListView.as_view(), name='products'),
	path('customers/<int:pk>/', customer, name='customer'),
	path('order/create', create_order, name='add_order'),
	path('order/update/<int:pk>', update_order, name='upd_order'),
	path('order/delete/<int:pk>', delete_order, name='del_order'),
	
]