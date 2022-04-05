from django.shortcuts import render

from catalog.models import Item


def home(request):
    template = 'homepage/home.html'
    items = Item.objects.published_tags()
    count = items.count()
    if not count:
        context = {}
    elif count < 3:
        context = {
            'items': items
        }
    else:
        context = {
            'items': items.random(3)
        }
    return render(request, template, context)
