from django import forms
from django.db.models import Avg, Count
from django.shortcuts import render, redirect

from catalog.models import Item, Category
from rating.models import Rating, User


class RatingUpdateForm(forms.Form):
    stars = forms.ChoiceField(choices=Rating.RATING_CHOICES, label='Выберите свое отношение', widget=forms.RadioSelect)


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
    stars = Rating.objects.filter(item=item, star__in=list(
        filter(lambda x: x != 0, map(lambda y: y[0], Rating.RATING_CHOICES)))).aggregate(Avg('star'), Count('star'))
    user = User.objects.filter(username=request.user.username).first()
    if user:
        user_star, _ = Rating.objects.get_or_create(user_id=user.id, item=item)
    else:
        user_star = None
    form = RatingUpdateForm(request.POST or None)
    if form.is_valid():
        user_star.star = form.cleaned_data['stars']
        user_star.save()
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
