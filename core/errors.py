from django.shortcuts import render


def page_not_found_view(request):
    return render(request, 'page-404.html', status=404)
