from django.contrib import admin

from .models import Category, Tag, Publication

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

class TagsInline(admin.StackedInline):
    model = Publication.tags.through
    extra = 0


@admin.register(Publication)
class AdminPublication(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'created']
    list_display_links = ['id', 'name','author', 'created']
    list_filter = ['tags', 'category', 'author']
    search_fields = ['name']
    inlines = [TagsInline]
