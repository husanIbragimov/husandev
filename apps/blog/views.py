from django.contrib.auth.models import User
from django.shortcuts import render

from apps.contact.models import GetInTouch
from apps.service.models import Category, Portfolio
from .models import BlogNews, AboutMe, Education, Experience, MeImages, Resume, MainImage


def index(request):
    # main page
    user = User.objects.last()
    about_qs = AboutMe.objects.prefetch_related('skills', 'experiences', 'educations', 'my_images').last()
    educations = Education.objects.all().order_by("-id")
    experiences = Experience.objects.all().order_by("-id")
    resume = Resume.objects.last()
    category = Category.objects.all().order_by('-id')
    portfolios = Portfolio.objects.all().order_by('-id')
    blogs = BlogNews.objects.all().prefetch_related('blogimages_set').order_by('-id')
    main_image = MainImage.objects.all().last()

    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        phone_number = request.POST.get('phone', None)
        message = request.POST.get('message', None)
        print(name, email, phone_number, message)

        GetInTouch.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            message=message
        )
        return render(request, 'index.html', {'success': 'Your message has been sent successfully.'})

    ctx = {
        "user": user,
        "resume": resume,
        "about": about_qs,
        "educations": educations,
        "experiences": experiences,

        'categories': category,
        'portfolios': portfolios,

        'main_image': main_image,

        'blogs': blogs
    }
    return render(request, 'index.html', ctx)
