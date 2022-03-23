from catalog.validators import validate_2_words, validate_brilliant
from core.models import PublishedBaseModel, SlugBaseModel
from django.db import models


class Category(PublishedBaseModel, SlugBaseModel):
    weight = models.PositiveSmallIntegerField("Вес", default=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.slug[:30]


class Tag(PublishedBaseModel, SlugBaseModel):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.slug[:30]


class Item(PublishedBaseModel):
    name = models.CharField(
        "Название", help_text="Макс 150 символов", max_length=150, null=True
    )
    text = models.TextField(
        "Описание",
        help_text="Минимум 2 слова",
        validators=[validate_brilliant, validate_2_words],
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="items",
        null=True,
        blank=True,
        verbose_name="Категория",
    )
    tags = models.ManyToManyField(Tag, related_name="tags", verbose_name="Теги")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name[:30]
