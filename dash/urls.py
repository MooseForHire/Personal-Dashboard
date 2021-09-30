from django.urls import path

#from . (current directory) import views
from . import views


urlpatterns = [
    # '' -> nothing after blog? yes. function views.home
    path('', views.home, name = 'dash-home'),

    #dash/about -> go to views.about
    path('about/',views.about, name = 'guyaki-about'),

    path('mydash/',views.mydash, name = 'guyaki-mydash'),
]