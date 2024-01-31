""" This module registers the models with the admin site. """
from django.contrib import admin
from .models import Follow, User

# Create your models here.
admin.site.register(User)
admin.site.register(Follow)
