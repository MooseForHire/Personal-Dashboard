from django.shortcuts import render, redirect
from .models import Tile
from users import views



#function based view = urls.py -> views.py -> templates
#class based view = list, detail, create, update, delete

def home(request):
    return render(request, 'dash/home.html')

def about(request):
    return render(request,'dash/about.html', {'title' : ':D'} )

def mydash(request):
    context = {
    'tiles': Tile.objects.all() 
    }
    return render(request,'dash/mydash.html', context)

def register(request):
    return render(request,'dash/register.html', {'title' : 'Registration'} )



