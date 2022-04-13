from django import forms
from django.db.models import Avg, Count
from django.shortcuts import render, redirect

from catalog.models import Item, Category
from rating.models import Rating, User


class RatingUpdateForm(forms.Form):
    RATING_CHOICES = [
        (0, 'Пусто'),
        (1, 'Ненависть'),
        (2, 'Неприязнь'),
        (3, 'Нейтрально'),
        (4, 'Обожание'),
        (5, 'Любовь')
    ]
    stars = forms.ChoiceField(choices=RATING_CHOICES, label='Выберите свое отношение', widget=forms.RadioSelect)


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
    stars = Rating.objects.filter(item=item, star__in=[1, 2, 3, 4, 5]).aggregate(Avg('star'), Count('star'))
    user = User.objects.get(username=request.user.username)
    user_star = Rating.objects.get(user_id=user.id)
    form = RatingUpdateForm(request.POST or None)
    if form.is_valid():
        user_star.star = form.cleaned_data['stars']
        user_star.save(update_fields=['star'])
        return redirect('item_detail', pk)

    context = {
        'pk': pk,
        'item': item,
        'stars': stars,
        'user': user,
        'user_star': user_star,
        'form': form
    }
    return render(request, template, context)
