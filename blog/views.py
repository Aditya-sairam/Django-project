from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from django.contrib import messages
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin





def Home(request):
	context = {
		'posts':Post.objects.all()

	}
	return render(request,'blog/home.html',context)

class userPostListView(ListView):
	model = Post 
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5 

	def get_queryset(self):
		user =  get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostListView(ListView):
	model = Post 
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5 





class PostDetailView(DetailView):
	model = Post 

class PostCreateView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','content','image']
	success_message = 'Your submission is sucessful!'
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)
		
		def get_success_message(self):
			return self.success_message

	

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
	model = Post
	fields = ['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True 
		return False



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/' 


	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True 
		return False




def About(request):
	return render(request,'blog/about.html',{'title':'about'})


class Communication(CreateView):
	model = Post
	fields = ['title','content']

def Soft(request):
	return render(request,'blog/soft.html')








