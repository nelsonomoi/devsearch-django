from django.db import models
from django.contrib.auth.models import User
import uuid


class Profiles(models.Model):
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True,null=False)
    email = models.EmailField(max_length=200,blank=True,null=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    short_intro = models.CharField(max_length=200,blank=True,null=True)
    bio = models.TextField()
    profile_image = models.ImageField(blank=True,null=True,upload_to = 'uploads',default='uploads/user-default.png')
    social_github = models.CharField(max_length=200,blank=True,null=False)
    social_twitter = models.CharField(max_length=200,blank=True,null=False)
    social_linkedin = models.CharField(max_length=200,blank=True,null=False)
    social_youtube = models.CharField(max_length=200,blank=True,null=False)
    social_website = models.CharField(max_length=200,blank=True,null=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


    def __str__(self):
        return self.user.username


class Skills(models.Model):
    owner = models.ForeignKey(Profiles,blank=True,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
