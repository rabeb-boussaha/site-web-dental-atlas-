from django.shortcuts import render

from django.views.generic import  View






def HomeViews(request):
    return render(request, 'X/home.html',) 

   
   

#def WishlistViews(request):
   #return render(request, 'registration/wishlist.html',)  