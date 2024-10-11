from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

# Create your models here.

    
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
    
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 
    
class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 
    
class Advertisement(models.Model):
    image = models.ImageField(upload_to='advertisement/')
    text =  models.CharField(max_length=150)





