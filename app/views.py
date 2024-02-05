from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .forms import UserUpdateForm,ProfileUpdateForm
import requests
import json
from pprint import pprint

def register (request):
    if request.method == 'POST':
         form =  UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, f'your account has been created! YOU are now able to login')
             return redirect('login')
    else:
       form =  UserRegisterForm()
    return render (request, "app/pages/register.html",  {'form':form}) 


@login_required
def profile(request):
    if request.method == 'POST':
       u_form = UserUpdateForm(request.POST, instance=request.user)
       p_form = ProfileUpdateForm(request.POST, 
                                  request.FILES, 
                                  instance=request.user.profile)
       if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request, f'your accout has been updated!')
           return redirect('profile')
       
    else:
         u_form = UserUpdateForm(instance=request.user)
         p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form 
    }

    return render(request, "app/pages/profile.html", context)


def home (request):
    res = requests.get(f"https://gogoanime-thullydev-api.onrender.com/recent-release")
    data = res.json()
    context = {
           "page": "home",
           "data": data,
    }
    return render (request, "app/pages/home.html", context)


def filter (request):
    res = requests.get("")
    data = res.json()
    context = {
           "page": "filter",
           "data": data,
    }
    return render (request, "app/pages/filter.html", context)


def  stream(request, video_id):
    res = requests.get(f"https://gogoanime-thullydev-api.onrender.com/vidcdn/watch/{video_id}")
    data = res.json()
    pprint(data)
    context = {
        "page":"watch",
        "data": data,
         "video_id": video_id,
        }
    return render (request, "app/pages/stream.html", context) 



def watch(request, video_id):
    context = {
        "page":"watch",
        "slug": video_id,
      
        }
    return render (request, "app/pages/watchpage.html", context)



def anime (request, anime_id):
    res = requests.get(f"https://gogoanime-thullydev-api.onrender.com/anime-details/{anime_id}")
    data = res.json()
    context = {
        "page":"anime",
        "data": data,
    }
    return render (request, "app/pages/anime.html", context) 



def stream(request, anime_id, video_id):
    # Fetch video details
    video_res = requests.get(f"https://gogoanime-thullydev-api.onrender.com/vidcdn/watch/{video_id}")
    video_data = video_res.json()
    pprint(video_data)

    # Fetch anime details
    anime_res = requests.get(f"https://gogoanime-thullydev-api.onrender.com/anime-details/{anime_id}")
    anime_data = anime_res.json()
    pprint(anime_data)

    context = {
        "page": "watch",
        "video_data": video_data,
        "anime_data": anime_data,
        "video_id": video_id,
    }
    return render(request, "app/pages/stream.html", context)
