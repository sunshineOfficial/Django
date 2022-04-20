from django import forms
from django.db.models import Avg, Count
from django.shortcuts import render, redirect

from catalog.models import Item, Category
from rating.models import Rating


class RatingUpdateForm(forms.Form):
    stars = forms.ChoiceField(choices=Rating.RATING_CHOICES, label='Выберите свое отношение', widget=forms.RadioSelect)


def item_list(request):
    template = 'catalog/list.html'
    categories = Category.objects.categories_and_items()
    context = {
        'categories': categories,
        'user': request.user
    }
    return render(request, template, context)


def item_detail(request, pk):
    template = 'catalog/detail.html'
    item = Item.objects.detailed_item(pk)
    stars = Rating.objects.filter(item=item, star__in=list(
        filter(lambda x: x != 0, map(lambda y: y[0], Rating.RATING_CHOICES)))).aggregate(Avg('star'), Count('star'))
    if request.user.is_authenticated:
        user_star = Rating.objects.filter(user=request.user, item=item).first()
    else:
        user_star = None
    form = RatingUpdateForm(request.POST or None)
    if form.is_valid():
        user_star.star = form.cleaned_data['stars']
        user_star.save()
        return redirect('item_detail', pk)
    context = {
        'item': item,
        'stars': stars,
        'user': request.user,
        'user_star': user_star,
        'form': form
    }
    return render(request, template, context)
