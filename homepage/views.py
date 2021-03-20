import telebot

from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .models import *
from .forms import ApplicationForm

bot = telebot.TeleBot('1596134202:AAF4rBcu3wD8D0sbjBqTnxhT0pVf3sdQzTY')


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


def contact(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            to_email = ['initmenthor@gmail.com',]
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            msg = f'Имя: {name} \nПочта: {email} \nТема{subject} \nСообщение: {message}'
            send_mail(subject, message, email, to_email, fail_silently=False)
            bot.send_message(959339948, msg)
    return redirect('index')