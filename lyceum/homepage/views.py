import random

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
            'items': items,
            'user': request.user
        }
    else:
        valid_ids = items.values_list('id', flat=True)
        random_ids = random.sample(list(valid_ids), 3)
        random_items = items.filter(id__in=random_ids)
        context = {
            'items': random_items,
            'user': request.user
        }
    return render(request, template, context)
