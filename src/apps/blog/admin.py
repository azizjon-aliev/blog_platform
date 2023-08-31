from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Admin interface for category model """

    date_hierarchy = "created_at"
    list_display = (
        'title',
        'slug',
        'created_at',
    )
    search_fields = (
        'title',
        'slug',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    prepopulated_fields = {
        'slug': ('title', )
    }
