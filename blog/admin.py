from django.contrib import admin
from . import models


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'id', 'status', 'slug', 'author']
    prepopulated_fields = {'slug' : ('tittle',), }



admin.site.register(models.Category)