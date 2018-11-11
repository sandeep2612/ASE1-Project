from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about.html/', views.about, name='blog-about'),
    path('cart.html/', views.cart, name='blog-cart'),
    path('shop.html/', views.shop, name='blog-shop'),
    path('contact.html/', views.contact, name='blog-contact'),
    ]
