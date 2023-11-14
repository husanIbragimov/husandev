from django.contrib import admin
from .models import Portfolio, Category, BannerDetail

admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(BannerDetail)
