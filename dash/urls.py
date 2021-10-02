from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users import views as user_views


urlpatterns = [

    path('', views.home, name = 'dash-home'),
    path('about/',views.about, name = 'guyaki-about'),
    path('mydash/',views.mydash, name = 'guyaki-mydash'),
    path('register/',views.register, name = 'guyaki-register'),

    ####################
   
]