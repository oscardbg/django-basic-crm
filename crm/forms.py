from crm.models import Product, Order, Customer
from django.forms import ModelForm

class CustomerForm(ModelForm):
	class Meta:
		model= Customer
		fields = '__all__'
		exclude = ['user']

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'