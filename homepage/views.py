from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    content1 = Home.objects.first()
    content2 = AboutMe.objects.first()
    hashtags = Hashtags.objects.all()
    certs = Certs.objects.all()
    skills = SkillLevel.objects.first()
    qualities = Qualities.objects.first()
    edu = Education.objects.all()
    exp = Experience.objects.all()
    return render(request, 'index.html', {
        'content1': content1,
        'content2': content2,
        'hashtags': hashtags,
        'certs': certs,
        'skills': skills,
        'qualities': qualities,
        'edu': edu,
        'exp': exp,
    })
