from django.contrib import admin
from .models import Image, Profile, Following

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Following)