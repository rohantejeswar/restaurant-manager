from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home_view(request):

	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'users/home.html', context)

def about_view(request):
	return render(request, 'users/about.html')
