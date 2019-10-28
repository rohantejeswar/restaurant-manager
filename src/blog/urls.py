from django.urls import path
from . import views

urlpatterns = [
	path('', views.PostListView.as_view(), name="blog-home"),
	path('post/<int:pk>/', views.PostDetailView.as_view(), name="blog-detail"),
	path('post/submit/', views.PostCreateView.as_view(), name="blog-create"),
]