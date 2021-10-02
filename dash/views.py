from django.shortcuts import render, redirect
from .models import Tile
from users import views



tiles = [
    {
        'author' : 'Caleb',
        'task' : 'First post',
        'content' : 'Content of my first post',
        'date_posted' : 'October 2021'
    },
    {
        'author' : 'Bob',
        'task' : 'Second post',
        'content' : 'Content of my second post',
        'date_posted' : 'October 1 2021'
    }
]


#Function to handle the traffic from the homepage to our dashboard
def home(request):

    #Return the home.html template
    #Still returns an http response still.
    return render(request, 'dash/home.html')

#About guyaki view
def about(request):
    return render(request,'dash/about.html', {'title' : ':D'} )

#-------------------------------------------------------------------#
def mydash(request):

    context = {
    'tiles': Tile.objects.all() 
    }
#--------------------------------------------------------------------#
    return render(request,'dash/mydash.html', context)

# This will handle the logic for the register view
def register(request):
    return render(request,'dash/register.html', {'title' : 'Registration'} )



