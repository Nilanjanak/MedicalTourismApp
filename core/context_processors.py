# core/context_processors.py

from shop.models import Category

def categories_context(request):
    return {
        'categories': Category.objects.all()
    }
