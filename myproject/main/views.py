from django.shortcuts import render, redirect

def index(request):
    return render(request, 'news/index.html')

def new(request):
    return render(request, 'news/news.html')

def about(request):
    return render(request, 'news/about.html')

def contact(request):
    return render(request, 'news/contact.html')

# Create your views here.
