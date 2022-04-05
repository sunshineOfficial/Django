from django.shortcuts import render

from catalog.models import Item, Category


def item_list(request):
    template = 'catalog/list.html'
    categories = Category.objects.categories_and_items()
    context = {
        'categories': categories
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
