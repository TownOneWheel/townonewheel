from django.db import models
from django.db.models.fields import NullBooleanField
from django.contrib.auth.models import User, update_last_login

from behavior import BaseField


class Cat(BaseField):
    catname = models.CharField(max_length=64)
    gender = models.CharField(max_length=20, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    neutering = models.CharField(max_length=10, null=True, blank=True)
    friendly = models.IntegerField(default='0')

    location = models.TextField()
    location_lat = models.FloatField(default=37.54490018658278)
    location_lon = models.FloatField(default=127.05685028171477)

    upload_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='upload', null=True, blank=True)
    # cat_like = models.TextField()

class CatImage(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.SET_NULL, related_name='image', null=True, blank=True)
    url = models.TextField(null=True, blank=True)

class Comment(BaseField):
    cat = models.ForeignKey(Cat, on_delete=models.SET_NULL, related_name='cat', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='writer', null=True, blank=True)
    content = models.TextField()