from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Profiles

def profiles(request):
    profiles = Profiles.objects.all()
    context = {'profiles': profiles}
    return render(request,'profiles.html',context)