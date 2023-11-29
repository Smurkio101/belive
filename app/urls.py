from django.urls import include, path
from . import views 

urlpatterns = [
    path('home', views.home, name='home'),
    path ('watchpage/<str:video_id>', views.watch, name='watchpage'), 
    path ('stream/<str:video_id>', views.stream, name='stream'), 
 ]