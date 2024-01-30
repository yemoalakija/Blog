"""This is the URL Configuration for the blog app."""
from django.urls import path
from .views import (
    blogs,
    category_blogs,
    tag_blogs,
    blog_details,
    add_reply,
    like_blog,
    search_blogs,
    my_blogs,
    add_blog,
    update_blog,
)

urlpatterns = [
    path("blogs/", blogs, name="blogs"),
    path("category_blogs/<str:slug>/", category_blogs, name="category_blogs"),
    path("tag_blogs/<str:slug>/", tag_blogs, name="tag_blogs"),
    path("blog/<str:slug>/", blog_details, name="blog_details"),
    path("add_reply/<int:blog_id>/<int:comment_id>/", add_reply, name="add_reply"),
    path("like_blog/<int:pk>/", like_blog, name="like_blog"),
    path("search_blogs/", search_blogs, name="search_blogs"),
    path("my_blogs/", my_blogs, name="my_blogs"),
    path("add_blog/", add_blog, name="add_blog"),
    path("update_blog/<str:slug>/", update_blog, name="update_blog"),
]
