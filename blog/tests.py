"""Tests for the blog app."""
from django.test import TestCase
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from user_profile.models import User
from .forms import TextForm, AddBlogForm
from .models import Category, Tag, Blog, Comment, Reply


# Create your tests here.
class TextFormTest(TestCase):
    """Test for TextForm form."""

    def test_text_form_valid(self):
        """Test for valid form data."""
        data = {"text": "This is a test text"}
        form = TextForm(data=data)
        self.assertTrue(form.is_valid())

    def test_text_form_invalid_empty_text(self):
        """Test for invalid form data."""
        data = {"text": ""}
        form = TextForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["text"], ["This field is required."])


class AddBlogFormTest(TestCase):
    """Test for AddBlogForm form."""

    def test_add_blog_form_valid(self):
        """Test for valid form data."""
        data = {
            "title": "Test Blog",
            "category": "Test Category",
            "banner": "test_banner.jpg",
            "description": "This is a test description",
        }
        form = AddBlogForm(data=data)
        self.assertTrue(form.is_valid())

    def test_add_blog_form_invalid_empty_fields(self):
        """Test for invalid form data."""
        data = {"title": "", "category": "", "banner": "", "description": ""}
        form = AddBlogForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"], ["This field is required."])
        self.assertEqual(form.errors["category"], ["This field is required."])
        self.assertEqual(form.errors["banner"], ["This field is required."])
        self.assertEqual(form.errors["description"], ["This field is required."])

    # Add more test cases as needed for specific validation scenarios

    def test_add_blog_form_description_field_type(self):
        """Test for description field type."""
        self.assertTrue(isinstance(AddBlogForm().fields["description"], RichTextField))

    def test_add_blog_form_meta_model(self):
        """Test for AddBlogForm Meta class model and fields."""
        self.assertEqual(AddBlogForm.Meta.model, Blog)
        self.assertEqual(
            AddBlogForm.Meta.fields, ["title", "category", "banner", "description"]
        )


class CategoryModelTest(TestCase):
    """Test for Category model."""

    def test_category_str_method(self):
        """Test for __str__ method."""
        category = Category(title="Test Category")
        self.assertEqual(str(category), "Test Category")

    def test_category_save_method(self):
        """Test for save method."""
        category = Category(title="Test Category")
        category.save()
        self.assertIsNotNone(category.slug)
        self.assertEqual(category.slug, slugify(category.title))


class TagModelTest(TestCase):
    """Test for Tag model."""

    def test_tag_str_method(self):
        """Test for __str__ method."""
        tag = Tag(title="Test Tag")
        self.assertEqual(str(tag), "Test Tag")

    def test_tag_save_method(self):
        """Test for save method."""
        tag = Tag(title="Test Tag")
        tag.save()
        self.assertIsNotNone(tag.slug)
        self.assertEqual(tag.slug, slugify(tag.title))


class BlogModelTest(TestCase):
    """Test for Blog model."""

    def setUp(self):
        """Set up objects for testing."""
        self.user = User.objects.create(username="testuser")
        self.category = Category.objects.create(title="Test Category")
        self.tag = Tag.objects.create(title="Test Tag")
        self.blog = Blog.objects.create(
            user=self.user,
            category=self.category,
            title="Test Blog",
            banner="test_banner.jpg",
            description="This is a test description",
        )

    def test_blog_str_method(self):
        """Test for __str__ method."""
        self.assertEqual(str(self.blog), "Test Blog")

    def test_blog_save_method(self):
        """Test for save method."""
        self.assertIsNotNone(self.blog.slug)
        self.assertEqual(self.blog.slug, slugify(self.blog.title))

    def test_blog_likes_field(self):
        """Test for likes field."""
        self.blog.likes.add(self.user)
        self.assertEqual(self.blog.likes.count(), 1)
        self.assertTrue(self.user in self.blog.likes.all())


class CommentModelTest(TestCase):
    """Test for Comment model."""

    def setUp(self):
        """Set up objects for testing."""
        self.user = User.objects.create(username="testuser")
        self.category = Category.objects.create(title="Test Category")
        self.blog = Blog.objects.create(
            user=self.user,
            category=self.category,
            title="Test Blog",
            banner="test_banner.jpg",
            description="This is a test description",
        )
        self.comment = Comment.objects.create(
            user=self.user, blog=self.blog, text="This is a test comment"
        )

    def test_comment_str_method(self):
        """Test for __str__ method."""
        self.assertEqual(str(self.comment), "This is a test comment")


class ReplyModelTest(TestCase):
    """Test for Reply model."""

    def setUp(self):
        """Set up objects for testing."""
        self.user = User.objects.create(username="testuser")
        self.category = Category.objects.create(title="Test Category")
        self.blog = Blog.objects.create(
            user=self.user,
            category=self.category,
            title="Test Blog",
            banner="test_banner.jpg",
            description="This is a test description",
        )
        self.comment = Comment.objects.create(
            user=self.user, blog=self.blog, text="This is a test comment"
        )
        self.reply = Reply.objects.create(
            user=self.user, comment=self.comment, text="This is a test reply"
        )

    def test_reply_str_method(self):
        """Test for __str__ method."""
        self.assertEqual(str(self.reply), "This is a test reply")
