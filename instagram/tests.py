from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Image, Following
# Create your tests here.
class TestProfileClass(TestCase):
    def setUp(self):
        self.user=User(username='kipkorir')
        self.user.save()
        self.profile_test = Profile(id=1, photo='home.jpg', bio='developer',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def save_method(self):
        self.profile_test.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles) >0)
    
    def delete_profile(self):
        self.profile_test.delete_profile()
        deleted_profiles=Profile.objects.all()
        self.assertTrue(len(deleted_profiles) ==0)

class TestImageClass(TestCase):
    def setUp(self):
        self.image=Image(name='burger')
        self.image.save()

        self.image=Image(id=2,name='burger', caption='delicious burger',comments='KFC burger')

        self.image.save_image()

        # adding a new image and saving it

        self.new_image=Image(name='ball')
        self.new_image.save()

    def delete_image(self):
        self.image.delete_image()
        self.image.delete()
    
    def update_caption(self):
        self.image.caption.update()
