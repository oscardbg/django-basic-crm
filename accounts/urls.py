from accounts.views import register_page, login_page, logout_page
from django.urls import path

app_name = 'accounts'

urlpatterns = [
	path('register/', register_page, name='register'),
	path('login/', login_page, name='login'),
	path('logout/', logout_page, name='logout')
]
