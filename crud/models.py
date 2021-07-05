from django.db import models
from django.db.models.fields import NullBooleanField
from social.models import Profile
from django.contrib.auth.models import User, update_last_login


class Cat(models.Model):
    catname = models.CharField(max_length=64)
    gender = models.CharField(max_length=20, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    neutering = models.CharField(max_length=10, null=True, blank=True)
    friendly = models.CharField(max_length=64, default='0')
    location = models.TextField()
    upload_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='upload', null=True, blank=True)
    # cat_like = models.TextField()

class CatImage(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.SET_NULL, related_name='image', null=True, blank=True)
    url = models.TextField(null=True, blank=True)

class Comment(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.SET_NULL, related_name='cat', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='writer', null=True, blank=True)
    content = models.TextField()