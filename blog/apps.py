"""Blog application configuration"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Blog application settings"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self) -> None:
        import blog.signals
