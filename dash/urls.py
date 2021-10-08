from django.urls import path
from . import views
from users import views as user_views


urlpatterns = [

    path('',views.home, name = 'dash-home'),
    path('about/',views.about, name = 'guyaki-about'),
    path('register/',views.register, name = 'guyaki-register'),
    path('dash/mydash/',views.mydash, name = 'guyaki-mydash'),
    path('profile/',user_views.profile, name = 'profile'),
    path('createTile/',views.createTile, name = 'create-tile'),
   
]    

