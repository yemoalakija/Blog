""" user_profile URL Configuration Options"""
from django.urls import path
from .views import (
    login_user,
    logout_user,
    register_user,
    profile,
    change_profile_picture,
    view_user_information,
    follow_or_unfollow_user,
    user_notifications,
    mute_or_unmute_user
)

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register_user/', register_user, name='register_user'),
    path('profile/', profile, name='profile'),
    path('change_profile_picture/', change_profile_picture, name='change_profile_picture'),
    path('view_user_information/<str:username>/', view_user_information, name="view_user_information"),
    path('follow_or_unfollow/<int:user_id>/', follow_or_unfollow_user, name='follow_or_unfollow_user'),
    path('user_notifications/', user_notifications, name='user_notifications'),
    path('mute_or_unmute_user/<int:user_id>/', mute_or_unmute_user, name='mute_or_unmute_user'),
]
