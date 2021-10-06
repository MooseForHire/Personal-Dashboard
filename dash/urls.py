from django.urls import path
from .views import TileListView
from . import views
from users import views as user_views


urlpatterns = [

    path('',TileListView.as_view(), name = 'dash-home'),
    path('about/',views.about, name = 'guyaki-about'),
    path('mydash/',TileListView.as_view(), name = 'guyaki-mydash'),
    path('register/',views.register, name = 'guyaki-register'),
    path('profile/',user_views.profile, name = 'profile')
    
] 

#<app>/<model>_viewtype>.html