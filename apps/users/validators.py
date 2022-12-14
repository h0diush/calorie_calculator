from django.core.exceptions import ValidationError


def validate_height_weight(value):
    if not value.isdigit():
        raise ValidationError('Должен состоять из цифр')
    if len(value) < 2:
        raise ValidationError('Разве такое существует')
    return value
