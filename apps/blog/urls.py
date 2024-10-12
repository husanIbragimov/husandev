from django.urls import path
from .views import HomeIndexView, BlogArchiveView, BlogDetailView, about, contact

app_name = 'blog'

urlpatterns = [
    path('', HomeIndexView.as_view(), name='home'),
    path('blogs/', BlogArchiveView, name='blog_list'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('about/', about, name='about'),
    path('more/', contact, name='contact'),
]
