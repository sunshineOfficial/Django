from django.shortcuts import render


def item_list(request):
    template = 'catalog/list.html'
    context = {}
    return render(request, template, context)


def item_detail(request, pk):
    template = 'catalog/detail.html'
    context = {
        'pk': pk
    }
    return render(request, template, context)
