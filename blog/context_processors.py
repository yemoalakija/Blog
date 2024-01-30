"""This module contains the context processor for the blog app."""
from .models import Category

# Register your models here.
def get_all_categories(request):
    """This function returns all categories."""
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return context
