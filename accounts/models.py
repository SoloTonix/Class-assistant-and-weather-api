from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    picture = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/', null=True)
    bio = models.TextField(null=True, blank=True)

    mobile = models.CharField(max_length=20,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=90, null=True, blank=True)

    career_path = models.CharField(max_length=20, null=True, blank=True)

    grade_points = models.DecimalField(default=0.00, validators=[MaxValueValidator(5)], max_digits=2, decimal_places=2, null=True, blank=True)
    achievements = models.TextField(null=True, blank=True)
    certificates = models.TextField(null=True, blank=True)



    def __str__(self):
        return f'{self.user.username}--profile'