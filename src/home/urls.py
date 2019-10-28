from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('menu/', views.menu_view, name='home-menu'),
    path('menu/cart/', views.cart_view, name='home-menu-cart'),
]