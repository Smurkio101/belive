from django.urls import include, path
from . import views 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('home', views.home, name='home'),
    path ('watchpage/<str:video_id>', views.watch, name='watchpage'), 
    path ('stream/<str:video_id>', views.stream, name='stream'), 
    path('filter', views.filter, name='filter'), 
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('anime/<str:anime_id>', views.anime, name='anime'),
]
     
 