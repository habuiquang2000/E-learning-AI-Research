from django.db.models import Count
from Document.models import Category


def category_list(req):
    categories = Category.objects.annotate(
        subject__count=Count("children")
    )
    return {
        "categories_template": categories
    }
