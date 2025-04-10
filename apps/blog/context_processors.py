from .models import Category, Tag, Publication


def categories(request):
    return {
        'context_categories': Category.objects.all(),
    }


def tags(request):
    return {
        'context_tags': Tag.objects.all(),
    }

def recent_publications(request):
    return {
        'context_recent_publications': Publication.objects.all().order_by('-created')[:8]
    }

