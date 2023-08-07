from django.shortcuts import render
from .models import BlogNews, AboutMe, Education, Experience, MeImages, Resume
from apps.service.models import BannerDetail, Category, Portfolio


def index(request):
    # main page
    about_qs = AboutMe.objects.all().last()
    educations = Education.objects.all().order_by("-id")
    experiences = Experience.objects.all().order_by("-id")
    my_images = MeImages.objects.filter(blog_id=about_qs).order_by('-id')
    resume = Resume.objects.last()
    category = Category.objects.all().order_by('-id')
    portfolios = Portfolio.objects.all().order_by('-id')
    blogs = BlogNews.objects.all().order_by('-id')
    ctx = {
        "resume": resume,
        "about": about_qs,
        "about_imgs": my_images,
        "educations": educations,
        "experiences": experiences,

        'categories': category,
        'portfolios': portfolios,

        'blogs': blogs
    }
    return render(request, 'index.html', ctx)
