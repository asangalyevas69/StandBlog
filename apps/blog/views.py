from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Publication, Category, Tag

def home(requests):
    # context = {
    #     'categories': Category.objects.all(),
    #     'tags': Tag.objects.all(),
    #     'publications': Publication.objects.all().order_by('-created')[:5]
    # }

    return render(request=requests, template_name='index.html')

def get_publications(request):
    publications = Publication.objects.all().order_by('-created')

    paginator = Paginator(object_list=publications, per_page=12 )

    page = request.GET.get('page', 1)
    publications = paginator.get_page(number=page)
    context = {
        'publications': publications
    #     'categories': Category.objects.all(),
    #     'tags': Tag.objects.all(),
    #     'publications': Publication.objects.all().order_by('-created')[:5]
     }
    return render(request=request, template_name='publications.html', context=context)

def get_publication(request, pk):

    publication = get_object_or_404(Publication, id=pk)

    context = {
        'publications': publication
    }
    return render(request, template_name='publication.html', context=context)
