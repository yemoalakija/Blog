""" User Profile App """
from django.apps import AppConfig

# Create your app config here.
class UserProfileConfig(AppConfig):
    """ User Profile Config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'
