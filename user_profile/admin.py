"""This module registers the User and Follow models with the admin site."""
from django.contrib import admin
from .models import User, Follow

# Register your models here.
admin.site.register(User)
admin.site.register(Follow)
