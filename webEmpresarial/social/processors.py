from .models import Links


def context_dict(request):
    context = {}
    links = Links.objects.all()
    for link in links:
        context[link.key] = link.url
    return context
