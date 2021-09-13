from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Following, Image, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()

    return render(request,"index.html", {"images":images})

def like(request, id):
    image=Image.objects.get(id=id)
    image.like=image.like+1

    print(image.like)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/accounts/login/')
def profile(request):
    profiles=Profile.objects.all()
    followers=Following.objects.filter(username=request.user.username)
    # print(followers)
    followings=Following.objects.filter(followed=request.user.username)

   

    return render(request,"profile.html", {'profiles':profiles,'followers':followers, 'following':followings})

def search(request):

    return render(request,"search.html")

def following(request,id):
    userTobefollowed=User.objects.get(id=id)
    currentUser=User.objects.get(id=request.user.id)
    print(currentUser.id)
    print(userTobefollowed.id)
    if userTobefollowed.id ==currentUser.id:
            print('you can\'t follow your self ')
            # folowerToremove=Followers(name=request.user.username,user_id=userTobefollowed.id,follower_id=request.user.url)
            # folowerToremove.remove(currentUser)
    else:
            print('no')
            folowerToadd=Following(username=currentUser.username,followed=userTobefollowed.username)
            print(folowerToadd)
            folowerToadd.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


