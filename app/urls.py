from django.urls import include, path
from . import views 

urlpatterns = [
    path('home', views.home, name='home')
    
 ]

urlpatterns = [
    path('watchpage', views.watchpage, name='watchpage')
]