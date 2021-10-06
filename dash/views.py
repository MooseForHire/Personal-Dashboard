from django.shortcuts import render
from .models import Tile
from django.views.generic import ListView


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

#class based view
class TileListView(ListView):
    model = Tile
    template_name = 'dash/mydash.html'
    context_object_name = 'tiles'
    ordering = ['-date_posted']


def register(request):
    return render(request,'dash/register.html', {'title' : 'Registration'} )



