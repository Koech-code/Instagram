from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Image, Following
# Create your tests here.
class TestProfileClass(TestCase):
    def setUp(self):
        self.user=User(username='kipkorir')
        self.user.save()

        self.profile_test = Profile(id=1, photo='home.jpg', bio='developer',
                                    user=self.user)