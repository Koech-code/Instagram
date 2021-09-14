from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .models import Following, Image, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()

    return render(request,"index.html", {"images":images})

def like(request, image_id):
    image=Image.objects.get(pk=image_id)
    current_user=request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except  Profile.DoesNotExist:
        raise Http404

    image.likes=image.likes+1
    print(image.likes)
    liked = True
    return HttpResponseRedirect(reverse('home')) 

@login_required(login_url='/accounts/login/')
def profile(request):
    profiles=Profile.objects.all()
    followers=Following.objects.filter(username=request.user.username)
    # print(followers)
    followings=Following.objects.filter(followed=request.user.username)

   

    return render(request,"profile.html", {'profiles':profiles,'followers':followers, 'following':followings})


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


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'people' in request.GET and request.GET["people"]:
        search_term = request.GET.get("people")
        searched_articles = User.objects.filter(username__contains=search_term)
        users=User.objects.all()
        print(users)
        message = f"{search_term}"
        print(searched_articles)
        array=[]
        for searched_articles in searched_articles:
            searched_articles=User.objects.get(id=searched_articles.id)
            array.append(searched_articles)
        return render(request, 'search.html',{"message":message,"user": array})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})