from django.db import models
from django_countries.fields import CountryField


class Hashtags(models.Model):
    hashtag = models.CharField(max_length=20)

    def __str__(self):
        return self.hashtag


class Home(models.Model):
    image = models.ImageField(upload_to='photo/')
    name = models.CharField(max_length=30)
    about_mini = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    link_tg = models.URLField(blank=True, null=True)
    link_inst = models.URLField(blank=True, null=True)
    link_tweet = models.URLField(blank=True, null=True)
    link_whatsapp = models.URLField(blank=True, null=True)
    link_git = models.URLField(blank=True, null=True)


class AboutMe(models.Model):
    about_me = models.TextField(max_length=500)
    age = models.CharField(max_length=3)
    residence = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    country = CountryField(null=True)
    city = models.CharField(max_length=30, null=True)

    block1 = models.TextField(max_length=150)
    block2 = models.TextField(max_length=150)
    block3 = models.TextField(max_length=150)
    block4 = models.TextField(max_length=150)

    clients = models.IntegerField()
    hours = models.IntegerField()
    projects = models.IntegerField()


# RESUME

class Education(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=30)
    school = models.CharField(max_length=30, null=True)
    description = models.TextField(max_length=150)


class Experience(models.Model):
    beginning_date = models.DateField()
    expiration_date = models.DateField()
    title = models.CharField(max_length=30)
    position = models.CharField(max_length=30, null=True)
    description = models.TextField(max_length=150)


class SkillLevel(models.Model):
    web_design = models.IntegerField(max_length=3)
    html_css = models.IntegerField(max_length=3)
    python = models.IntegerField(max_length=3)
    frameworks = models.IntegerField(max_length=3)


class Qualities(models.Model):
    first = models.IntegerField(max_length=3)
    second = models.IntegerField(max_length=3)
    third = models.IntegerField(max_length=3)
    fourth = models.IntegerField(max_length=3)


class Certs(models.Model):
    image = models.ImageField(upload_to='cert/')
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=150)
    date = models.DateField()
    
