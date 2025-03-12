from django.shortcuts import render
from .models import BlogNews, AboutMe, Education, Experience, MeImages, Resume, MainImage
from apps.service.models import BannerDetail, Category, Portfolio
from apps.contact.models import GetInTouch


def index(request):
    # main page
    about_qs = AboutMe.objects.prefetch_related('experiences', 'educations', 'my_images').last()
    educations = Education.objects.all().order_by("-id")
    experiences = Experience.objects.all().order_by("-id")
    resume = Resume.objects.last()
    category = Category.objects.all().order_by('-id')
    portfolios = Portfolio.objects.all().order_by('-id')
    blogs = BlogNews.objects.all().order_by('-id')
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
