from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', view=views.home, name='index'),
    path('publications/', view=views.get_publications, name='publications'),
    path('publications/<int:pk>', view=views.get_publication, name='publication')
]
