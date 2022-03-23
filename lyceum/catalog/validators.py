from django.core.exceptions import ValidationError


def validate_2_words(value):
    value = value.split()
    k = 0
    for el in value:
        if not el.isdigit():
            k += 1
        if k == 2:
            break

    if k < 2:
        raise ValidationError('Минимум 2 слова')


def validate_brilliant(value):
    must_words = {'превосходно', 'роскошно'}
    cleaned_text = set(value.lower().split())
    difference = must_words - cleaned_text
    if len(difference) == len(must_words):
        raise ValidationError(f'Обязательно используйте слова: {", ".join(must_words)}')
