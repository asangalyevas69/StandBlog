from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', view=views.home, name='index')
]
