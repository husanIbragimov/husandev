from collections import defaultdict

from django.db.models import CharField
from django.db.models import F, Value
from django.db.models.functions import Concat
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from .models import Blog


class HomeIndexView(ListView):
    template_name = 'blog/index.html'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogArchiveView(ListView):
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True) \
            .prefetch_related('tags') \
            .annotate(year=F("created_at__year"),
                      get_absolute_url=Concat(Value('/blog/'), 'slug', Value('/'), output_field=CharField())) \
            .values("title", "slug", "created_at", "year", "get_absolute_url")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        blogs_by_year = defaultdict(list)
        for blog in queryset:
            blogs_by_year[blog['year']].append(blog)

        context['blogs_by_year'] = dict(blogs_by_year)
        return context


BlogArchiveView = cache_page(60 * 15)(BlogArchiveView.as_view())


class BlogDetailView(SingleObjectMixin, ListView):
    template_name = 'blog/blog_detail.html'
    context_object_name = 'object'
    slug_url_kwarg = 'slug'
    queryset = Blog.objects.filter(is_published=True)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=self.get_queryset().prefetch_related('tags'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all() if self.object.tags.exists() else []
        return context


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')
