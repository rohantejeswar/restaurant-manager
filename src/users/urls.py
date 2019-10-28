from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
	path('register/', views.register_view, name='users-register'),
	path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='users-login'),
	path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
	path('profile/', views.profile_view, name='users-profile'),
]