from django.shortcuts import render
from django.views.generic import ListView

from .models import Blog


class HomeIndexView(ListView):
    template_name = 'blog/index.html'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogArchiveView(ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).annotate("created_at")


class BlogDetailView(ListView):
    template_name = 'blog/blog_detail.html'
    context_object_name = 'object'

    def get_queryset(self):
        return Blog.objects.filter(slug=self.kwargs['slug']).first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_queryset()
        context['tags'] = self.get_queryset().tags.all()
        return context


def about(request):
    return render(request, 'blog/about.html')
