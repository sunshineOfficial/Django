from django.shortcuts import render

from catalog.models import Item


def item_list(request):
    template = 'catalog/list.html'
    items = Item.objects.published_tags()
    count = items.count()
    if not count:
        context = {}
    else:
        context = {
            'items': items
        }
    return render(request, template, context)


def item_detail(request, pk):
    template = 'catalog/detail.html'
    item = Item.objects.detailed_item(pk)
    context = {
        'pk': pk,
        'item': item
    }
    return render(request, template, context)
