from django.views import generic
from django.shortcuts import render

def home_page(request):
    context = {
        'current':'home'
    }
    return render(request, 'geodjango/home.html',context)

def about_page(request):
    context = {
        'current':'about'
    }
    return render(request, 'geodjango/about.html',context)

def portfolio_page(request):
    context = {
        'current':'portfolio'
    }
    return render(request, 'geodjango/portfolio.html',context)

def blog_page(request):
    context = {
        'current':'blog'
    }
    return render(request, 'geodjango/blog.html',context)
