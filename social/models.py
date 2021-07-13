from django.db import models
from django.contrib.auth.models import User
from crud.models import Cat

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=8)
    profile_img_url = models.TextField()
    introduction = models.TextField()
    email = models.EmailField()
    created_at = models.TextField()
    updated_at = models.TextField(null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) :
        return str(self.user)
        
class Relationship(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='relationship', null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    favorite_cat = models.ManyToManyField(Cat, related_name='catrelationship', blank=True)

