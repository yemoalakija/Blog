"""This file is used to register the Blog model with the admin site."""
from django.contrib import admin
from .models import Category, Tag, Blog, Comment, Reply


# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)
