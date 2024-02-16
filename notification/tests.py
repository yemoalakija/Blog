"""Tests for the notification app."""
from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from blog.models import Blog
from user_profile.models import User
from .models import Notificaiton


# Create your tests here.
class NotificationModelTest(TestCase):
    """Tests for the Notification model."""

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(username="testuser")

        # Create a blog for testing
        self.blog = Blog.objects.create(
            user=self.user,
            title="Test Blog",
            category="Test Category",
            banner="test_banner.jpg",
            description="Test description",
        )

    def test_notification_creation(self):
        """Test the creation of a notification."""
        # Create a notification
        notification = Notificaiton.objects.create(
            content_type=ContentType.objects.get_for_model(Blog),
            object_id=self.blog.id,
            content_object=self.blog,
            user=self.user,
            text="New blog post!",
            notification_types="Blog",
        )

        # Check if the notification is created successfully
        self.assertEqual(notification.user, self.user)
        self.assertEqual(notification.content_object, self.blog)
        self.assertEqual(notification.notification_types, "Blog")
        self.assertFalse(notification.is_seen)  # Default value should be False
        self.assertIsNotNone(notification.created_date)

    def test_notification_str_method(self):
        """Test the __str__ method of the Notification model."""
        # Create a notification
        notification = Notificaiton.objects.create(
            content_type=ContentType.objects.get_for_model(Blog),
            object_id=self.blog.id,
            content_object=self.blog,
            user=self.user,
            text="New blog post!",
            notification_types="Blog",
        )

        # Check the __str__ method
        expected_str = "New blog post!"
        self.assertEqual(str(notification), expected_str)
