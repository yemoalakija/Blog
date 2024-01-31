""" User Profile App """
from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    """ User Profile Config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'
