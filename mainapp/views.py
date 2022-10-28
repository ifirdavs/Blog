from django.shortcuts import render, redirect
from django.views import View
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

class BlogView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'articles': Article.objects.filter(author__user=request.user),
                
            }
            return render(request, 'blog.html', data)
        return redirect('/login')

    def post(self, request):
        Article.objects.create(
            head=request.POST.get('head'),
            date=request.POST.get('date'),
            topic=request.POST.get('topic'),
            text=request.POST.get('text'),
            author=Author.objects.get(user=request.user),
        )
        return redirect('/blog')

class ArticleView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            data = {
                'article': Article.objects.get(id=pk),
            }
            return render(request, 'article.html', data)
        return redirect('login')                           ## name ='login'

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            return redirect('login')
        login(request, user)
        return redirect('/blog')

def logoutView(request):
    logout(request)
    return redirect('/')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
        
        Author.objects.create(
            name=request.POST.get('name'),
            age=request.POST.get('age'),
            job=request.POST.get('job'),
            user = user,
        )

        return redirect('login')            ## name="login"