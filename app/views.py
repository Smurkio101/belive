from django.shortcuts import render
from django.http import HttpResponse
def home (request):
    context = {
           "page": "home"
    }
    return render (request, "app/pages/home.html", context)

def watch(request, video_id):
    context = {
        "page":"watch"
        }
    return render (request, "app/pages/watchpage.html", context)
      
def  stream(request, video_id):
    context = {
        "page":"stream"
        }
    return render (request, "app/pages/stream.html", context) 
       
  