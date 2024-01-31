""" Manages the user model """
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class User(AbstractUser):
    """ User model """
    email = models.EmailField(
        max_length=150,
        unique=True,
        error_messages={
            "unique": "The email must be unique"
        }
    )
    profile_image = models.ImageField(
        upload_to="images/", default="../default_profile_jldl6ng"
    )
    followers = models.ManyToManyField("Follow")

    REQUIRED_FIELDS = ["email"]
    objects = CustomUserManager()

    def __str__(self):
        return str(self.username)

    def get_profile_picture(self):
        """Return the profile picture url"""
        url = ""
        try:
            url = self.profile_image.url
        except FileNotFoundError:
            url = ""
        return url


class Follow(models.Model):
    """ Follow model """
    followed = models.ForeignKey(
        User,
        related_name='user_followers',
        on_delete=models.CASCADE
    )
    followed_by = models.ForeignKey(
        User,
        related_name='user_follows',
        on_delete=models.CASCADE
    )
    muted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.followed_by.username} started following {self.followed.username}"
