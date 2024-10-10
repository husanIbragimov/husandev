from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.shortcuts import render
from django.urls import path

from .models import Blog, Tag

admin.site.register(Tag)

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        fields = '__all__'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'created_at', 'is_published']
    list_filter = ['is_published']
    search_fields = ['title', 'content']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    filter_horizontal = ['tags']
    # prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    save_on_top = True
    save_as = True
    list_per_page = 10
    actions = ['make_published', 'make_unpublished']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:pk>/preview/', self.admin_site.admin_view(self.preview), name='blog_preview'),
        ]
        return custom_urls + urls

    @admin.display(description='Preview')
    def preview(self, request, slug, *args, **kwargs):
        blog_post = Blog.objects.get(slug=slug)
        context = {'blog_post': blog_post}
        return render(request, 'admin/blog/preview.html', context)

    @staticmethod
    def make_published(request, queryset):
        queryset.update(is_published=True)

    make_published.short_description = 'Mark selected blogs as published'

    @staticmethod
    def make_unpublished(request, queryset):
        queryset.update(is_published=False)

    make_unpublished.short_description = 'Mark selected blogs as unpublished'
