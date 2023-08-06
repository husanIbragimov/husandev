from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime


class Resume(models.Model):
    resume = models.FileField(upload_to='media/resume/', null=True)
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
    birthday = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=17, null=True, blank=True)
    degree = models.CharField(max_length=15, null=True, blank=True)
    interest = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    @property
    def get_age(self):
        current_age = datetime.now().date().year - self.birthday.year
        print(current_age)
        self.age = current_age
        self.save()
        return current_age

    def __str__(self):
        return f"{self.title}"


class Experience(models.Model):
    blog = models.ForeignKey(AboutMe, on_delete=models.CASCADE, null=True, blank=True, related_name='experiences')
    experience = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=31, null=True, blank=True)
    period = models.CharField(max_length=47, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.experience} - {self.period}"


class Education(models.Model):
    blog = models.ForeignKey(AboutMe, on_delete=models.CASCADE, null=True, blank=True, related_name='educations')
    education = models.CharField(max_length=50, null=True, blank=True)
    degree = models.CharField(max_length=15, null=True, blank=True)
    period = models.CharField(max_length=15)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.education} - {self.period}"


class MeImages(models.Model):
    blog = models.ForeignKey(AboutMe, on_delete=models.CASCADE, null=True, blank=True, related_name='my_images')
    image = models.ImageField(upload_to=f'media/about_me/', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Theme: {self.blog}. image: {self.image}"
