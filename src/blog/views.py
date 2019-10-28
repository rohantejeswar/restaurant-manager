from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

def home_view(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('blog-detail', kwargs={'pk': self.object.id})