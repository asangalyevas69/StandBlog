from django.shortcuts import render

from .models import Publication, Category, Tag

def home(requests):
    context = {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
        'publications': Publication.objects.all().order_by('-created')[:5]
    }

    return render(requests, 'index.html', context=context)
