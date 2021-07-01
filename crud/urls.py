from django.contrib import admin
from django.urls import path
from .views import AddView


app_name = 'crud'

urlpatterns = [
    path('add/', AddView.as_view(), name='add'),
]