from django.db import models


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        abstract = True


class SlugBaseModel(models.Model):
    slug = models.SlugField(
        'Название',
        help_text='Макс 200 символов',
        max_length=200,
        unique=True,
        null=True,
    )

    class Meta:
        abstract = True
