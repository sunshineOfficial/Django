from django.db import models
from django.db.models import Prefetch
from django.http import Http404
from django_random_queryset import RandomManager

from catalog.validators import validate_2_words, validate_brilliant
from core.models import NameBaseModel, PublishedBaseModel, SlugBaseModel


class CategoryManager(models.Manager):
    def categories_and_items(self):
        return self.get_queryset().filter(is_published=True).order_by('-weight').only('name').prefetch_related(
            Prefetch('items', queryset=Item.objects.filter(is_published=True)))


class Category(NameBaseModel, PublishedBaseModel, SlugBaseModel):
    weight = models.PositiveSmallIntegerField('Вес', default=100)
    objects = CategoryManager()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name[:30]


class Tag(NameBaseModel, PublishedBaseModel, SlugBaseModel):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name[:30]


class ItemManager(RandomManager):
    def published_tags(self):
        return self.get_queryset().filter(is_published=True).only('name', 'text').prefetch_related(
            Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only('name')))

    def detailed_item(self, pk):
        try:
            return self.get_queryset().filter(is_published=True, pk=pk).select_related('category').only(
                'name', 'category__name', 'text').prefetch_related(
                Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only('name'))).get()
        except Item.DoesNotExist:
            raise Http404


class Item(NameBaseModel, PublishedBaseModel):
    text = models.TextField(
        'Описание',
        help_text='Минимум 2 слова',
        validators=[validate_brilliant, validate_2_words],
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='items',
        null=True,
        blank=True,
        verbose_name='Категория'
    )
    tags = models.ManyToManyField(Tag, related_name='items', verbose_name='Теги')
    objects = ItemManager()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name[:30]
