from django.contrib import admin
from .models import *


class BlogImagesInline(admin.StackedInline):
    model = BlogImages
    extra = 1


@admin.register(BlogNews)
class BlogNewsAdmin(admin.ModelAdmin):
    inlines = [BlogImagesInline]
    list_display = ('title', 'created_at', 'id')


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1
    readonly_fields = ('created_at',)


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    readonly_fields = ('created_at',)


class MeImagesInline(admin.TabularInline):
    model = MeImages
    extra = 1


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    inlines = [MeImagesInline, ExperienceInline, EducationInline]
    list_display = ('title', 'age')
    # readonly_fields = ('my_age',)


admin.site.register(Resume)
admin.site.register(MeImages)
admin.site.register(Education)
admin.site.register(MainImage)
admin.site.register(Experience)
