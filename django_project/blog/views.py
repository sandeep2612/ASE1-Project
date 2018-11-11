from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def cart(request):
    return render(request, 'blog/cart.html', {'title': 'cart'})

def shop(request):
    return render(request, 'blog/shop.html', {'title': 'shop'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'contact'})
