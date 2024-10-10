import uuid

from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Tag(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255, blank=False, null=False, unique=True)
    introduction = models.CharField(blank=True, null=True, max_length=500)
    content = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='blog/images/', blank=True, null=True)
    image_link = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{uuid.uuid4()}"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug})

    def get_image_url(self):
        if self.image:
            return self.image.url
        return "https://via.placeholder.com/800x400.png?text=No+Image"

    def get_previous_blog_url(self):
        previous_blog = Blog.objects.filter(id__lt=self.id).first()
        if previous_blog:
            return previous_blog.get_absolute_url()
        return self.get_absolute_url()

    def get_next_blog_url(self):
        next_blog = Blog.objects.filter(id__gt=self.id).first()
        if next_blog:
            return next_blog.get_absolute_url()
        return self.get_absolute_url()
