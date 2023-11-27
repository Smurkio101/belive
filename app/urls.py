from django.urls import include, path
from . import views 

urlpatterns = [
    path('home', views.home, name='home'),
    path ('watchpage/<str:watch_id>', views.watch, name='watchpage'), 

 ]
