from django.shortcuts import render
from .models import *
from django.http import FileResponse


def index(request):
    photos = Photo.objects.all()

    contex = {
        "photos":Photo.objects.all()
    }
    return render(request,"index.html",contex)
def browse(request):
    photos = Photo.objects.all()
    
    contex = {
        "photos":Photo.objects.all()    
    }
    return render(request,"browse ads.html",contex)
def about(request):
    
    contex = {
        
    }
    return render(request,"about.html",contex)
def clients(request):   
    contex = {
        
    }
    return render(request,"clients.html",contex)
def contact(request):   
    contex = {
        
    }
    return render(request,"contact.html",contex)
def footer(request):   
    contex = {
        
    }
    return render(request,"footer.html",contex)