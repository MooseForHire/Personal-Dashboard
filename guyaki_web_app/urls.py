from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#importing views from app 'users'
from users import views as user_views


#url pattern -> url mapping
urlpatterns = [

    path('admin/', admin.site.urls),
    path('dash/', include('dash.urls')),
    path('register/', user_views.register, name = 'register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'),
    path('profile/',user_views.profile, name = 'profile')
    
]

#only in debug mode! 
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()