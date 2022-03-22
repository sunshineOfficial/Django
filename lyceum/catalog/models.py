from django.db import models

from catalog.validators import validate_brilliant, validate_2_words
from core.models import PublishedBaseModel


class Category(PublishedBaseModel):
    slug = models.SlugField('Категория', help_text='Макс 200 символов', max_length=200, unique=True, null=True)
    weight = models.PositiveSmallIntegerField('Вес', default=100)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

    def __str__(self):
        return self.slug[:15]


class Tag(PublishedBaseModel):
    slug = models.SlugField('Тег', help_text='Макс 200 символов', max_length=200, unique=True, null=True)

    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    

    def __str__(self):
        return self.slug[:15]


class Item(PublishedBaseModel):
    name = models.CharField('Название', help_text='Макс 150 символов', max_length=150, null=True)
    text = models.TextField('Описание', help_text='Минимум 2 слова', validators=[validate_brilliant, validate_2_words], null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items', null=True, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, related_name='tags', verbose_name='Теги')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return self.text[:15]
