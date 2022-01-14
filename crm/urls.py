from crm.views import delete_order, home, dashboard, ProductListView, customer, create_order, update_order, delete_order, register_page, login_page, logout_page
from django.urls import path

app_name = 'crm'

urlpatterns = [
	path('', home, name='home'),
	path('dashboard/', dashboard, name='dashboard'),
	path('products/', ProductListView.as_view(), name='products'),
	path('customers/<int:pk>/', customer, name='customer'),
	path('order/create/<int:pk>', create_order, name='add_order'),
	path('order/update/<int:pk>', update_order, name='upd_order'),
	path('order/delete/<int:pk>', delete_order, name='del_order'),
	path('register/', register_page, name='register'),
	path('login/', login_page, name='login'),
	path('logout/', logout_page, name='logout')
]