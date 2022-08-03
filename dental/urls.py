from django import views
from . import views
from .views import *
from django.urls import include, path
from django.contrib.auth import views as auth_views


app_name = 'dental'

urlpatterns = [
    #path('', include("django.contrib.auth.urls")),
    path('home/', views.HomeViews ,name='home')
     
   #path('wishlist/', views.WishlistViews, name="wishlist"),
]
