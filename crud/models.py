from django.db import models
from social.models import Profile
from django.contrib.auth.models import User


class Cat(models.Model):
    COLOR_CHOICES = {
        ('YELLOW', '노란색'),
        ('BLACK', '검은색'), 
        ('GRAY', '회색'), 
        ('WHITE', '하얀색')
    }
    GENDER_CHOICES = {
        ('MALE', '수컷'),
        ('FEMALE', '암컷'),
        ('DONT_KNOW', '모름')
    }
    NEUTERING_CHOICES = {
        ('O', 'O'),
        ('X', 'X'),
        ('DONT_KNOW', '모름')
    }
    catname = models.CharField(max_length=64)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, null=True, blank=True)
    neutering = models.CharField(max_length=10, choices=NEUTERING_CHOICES, null=True, blank=True)
    friendly = models.CharField(max_length=64, default='0')
    location = models.TextField()
    upload_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='upload', null=True, blank=True)
    # cat_like = models.TextField()

class CatImage(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.SET_NULL, related_name='image', null=True, blank=True)
    url = models.TextField(null=True, blank=True)