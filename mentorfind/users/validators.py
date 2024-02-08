from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def uppercase_letter_validation(value):
    if value.lower() == value:
        raise ValidationError(
            _(f'Ensure this value has an uppercase letter.'),
            params={"value": value},
        )