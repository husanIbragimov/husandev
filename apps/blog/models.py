from django.db import models
from ckeditor.fields import RichTextField


class Resume(models.Model):
    resume = models.ImageField(upload_to='media/resume/', null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at}"


class BlogNews(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class BlogImages(models.Model):
    blog = models.ForeignKey(BlogNews, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to=f'media/blog_images/', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Blog: {self.blog}. image: {self.image}"


class AboutMe(models.Model):
    title = models.CharField(max_length=225, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class MeImages(models.Model):
    blog = models.ForeignKey(AboutMe, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to=f'media/about_me/', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Theme: {self.blog}. image: {self.image}"
