from django.shortcuts import render
from django.http import HttpResponse
def home (request):
    context = {
           "page": "home"
    }
    return render (request, "app/pages/home.html", context)
def watch(request, video_id):
       video_id = {
              "page":"watch"
              
       }
       return render (HttpResponse, "app/pages/watchpage.html",video_id)
       
       