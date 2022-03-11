from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

# Create your models here.
class corousel(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title
class Plan(models.Model):
    desc = models.TextField(max_length=200)
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
class Employes (models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class VideoMedia (models.Model):
    video = models.FileField(upload_to='video',validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    def __str__(self):
        return 'Video'
class Client (models.Model):
    description = models.TextField(max_length=500)
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name
class Contact (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    comment=models.TextField(max_length=500)
    phonnumber = models.CharField(max_length=50)
    def __str__(self):
        return self.email

class Blog(models.Model):
    img = models.ImageField(upload_to='media/blog')
    title = models.CharField(max_length=50)
    description = models.TextField()
    datetime = models.DateField(auto_now=True)
    def __str__(self):
        return self.title
class Blog1(models.Model):
    USER_MODEL = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media/blog')
    title = models.CharField(max_length=50)
    description = models.TextField()
    datetime = models.DateField(auto_now=True)
    def __str__(self):
        return self.title