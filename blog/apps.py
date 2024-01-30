"""This file is used to configure the blog app."""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """This class is used to configure the blog app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        """This method is called when the blog app is ready."""
        import blog.signals
