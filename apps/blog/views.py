from django.shortcuts import render
from .models import BlogNews, AboutMe, Education, Experience, MeImages, Resume
from apps.service.models import BannerDetail


def index(request):
    # main page
    about_qs = AboutMe.objects.all().last()
    educations = Education.objects.all().order_by("-id")
    experiences = Experience.objects.all().order_by("-id")
    my_images = MeImages.objects.filter(blog_id=about_qs).order_by('-id')
    resume = Resume.objects.last()
    ctx = {
        "resume": resume,
        "about": about_qs,
        "about_imgs": my_images,
        "educations": educations,
        "experiences": experiences
    }
    return render(request, 'index.html', ctx)
