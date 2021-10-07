from django.shortcuts import render,redirect
from .models import Tile, Category



#function based view = urls.py -> views.py -> templates
#class based view = list, detail, create, update, delete


def home(request):
    context = {
        'tiles' : Tile.objects.all()
    }
    return render(request, 'dash/home.html', context)


def about(request):
    return render(request,'dash/about.html', {'title' : ':D'} )

def mydash(request):
    return render(request,'dash/mydash.html')


def createTile(request):
    return render(request, 'dash/tile_form.html')

def register(request):
    return render(request,'users/register.html', {'title' : 'Registration'} )


