from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	picture = models.ImageField(default='profileImg.png', null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORIES = (
		('Indoor', 'Indoor'), ('Out door', 'Out door')
	)

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORIES)
	description = models.TextField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')
	)

	customer = models.ForeignKey(Customer, related_name='orders', null=True, on_delete=models.SET_NULL)
	product = models.ForeignKey(Product, related_name='orders', null=True, on_delete=models.SET_NULL)
	date_create = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.TextField(null=True)

	def __str__(self):
		return f'Order: {self.product.name} '