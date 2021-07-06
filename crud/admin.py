from django.contrib import admin
from .models import Cat, CatImage, Comment

admin.site.register(Cat)
admin.site.register(CatImage)
admin.site.register(Comment)