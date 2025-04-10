from django.db import models
from apps.users.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Publication(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='publications'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='publications'
    )
    tags = models.ManyToManyField(
        Tag, related_name='publications', blank=True
    )
    image = models.ImageField(upload_to='publications', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='Title')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name