from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from catalog.models import Item

User = get_user_model()


class Rating(models.Model):
    RATING_CHOICES = [
        (0, 'Пусто'),
        (1, 'Ненависть'),
        (2, 'Неприязнь'),
        (3, 'Нейтрально'),
        (4, 'Обожание'),
        (5, 'Любовь')
    ]
    star = models.PositiveSmallIntegerField(
        'Рейтинг',
        help_text='От 1 до 5',
        choices=RATING_CHOICES,
        default=0,
        validators=[validators.MaxValueValidator(5)],
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='rating',
        null=True,
        verbose_name='Пользователь',
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='rating',
        null=True,
        verbose_name='Товар',
    )

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        constraints = [
            models.UniqueConstraint(fields=['user', 'item'], name='unique_like')
        ]

    def __str__(self):
        return self.get_star_display()
