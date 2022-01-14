from crm.models import Product, Order, Customer
from django.forms import ModelForm

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'