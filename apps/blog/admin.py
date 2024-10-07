from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'is_published']
    list_filter = ['is_published']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    save_on_top = True
    save_as = True
    list_per_page = 10
    actions = ['make_published', 'make_unpublished']

    def make_published(self, request, queryset):
        queryset.update(is_published=True)

    make_published.short_description = 'Mark selected blogs as published'

    def make_unpublished(self, request, queryset):
        queryset.update(is_published=False)

    make_unpublished.short_description = 'Mark selected blogs as unpublished'
