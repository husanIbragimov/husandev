from django.db import models


class BannerDetail(models.Model):
    avatar = models.ImageField(upload_to='media/avatar/', null=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    motto = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=225, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to='media/portfolio/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    code = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
