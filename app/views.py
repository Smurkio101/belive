from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .forms import UserUpdateForm,ProfileUpdateForm
import requests
import json
from pprint import pprint



      
def  stream(request, video_id):
    context = {
        "page":"stream"
        }
    return render (request, "app/pages/stream.html", context) 

def filter (request):
    context = {
           "page": "filter"
    }
    return render (request, "app/pages/filter.html", context) 

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






def watch(request, video_id):
    res = requests.get("https://gogoanime-thullydev-api.onrender.com/anime-details/naruto")
    data = res.json()
    pprint(data)
    context = {
        "page":"watch",
        "data": data,
        }
    return render (request, "app/pages/watchpage.html", context)

def home (request):
    res = requests.get("https://gogoanime.consumet.stream/recent-release")
    data = res.json()
    pprint(data)
    context = {
           "page": "home",
           "data": data,
    }
    return render (request, "app/pages/home.html", context)


def filter (request):
    res = requests.get("https://gogoanime.consumet.stream/recent-release")
    data = res.json()
    pprint(data)
    context = {
           "page": "filter",
           "data": data,
    }
    return render (request, "app/pages/filter.html", context)