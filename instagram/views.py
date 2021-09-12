from django.shortcuts import render
from .models import Image, Profile
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    images = Image.objects.all()

    return render(request,"app/index.html", {"images":images})

def profile(request):
    


    return render(request,"app/profile.html")

def search(request):

    return render(request,"app/search.html")


