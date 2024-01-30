"""This file is used to create forms for blog app"""
from django import forms
from ckeditor.fields import RichTextField
from .models import Blog


class TextForm(forms.Form):
    """This class is used to create a form for text"""

    text = forms.CharField(widget=forms.Textarea, required=True)


class AddBlogForm(forms.ModelForm):
    """This class is used to create a form for blog"""

    description = RichTextField()

    class Meta:
        """Meta class for blog form"""

        model = Blog
        fields = ("title", "category", "banner", "description")
