""" Context processors for blog app. """
from .models import Category


def get_all_categories(request):
    """ Get all categories. """
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return context
