from django.db import models


from django.contrib.auth.models import User   # user is uilt in table to register our users data
# Create your models here.

class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField()           # for using image field and text field we need to install pillow package
    address=models.TextField()                # in forms we don't have textfield but for models we have