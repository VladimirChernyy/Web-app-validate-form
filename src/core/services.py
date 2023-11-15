import copy

from app.models import TemplateFormModel
from core.validators import (
    validate_email,
    validate_phone,
    validate_date,
)


def find_matching_form(input_fields):
    for template in TemplateFormModel.objects.all():
        template_fields_name = template.data
        template_fields = copy.deepcopy(template_fields_name)
        template_fields.pop('name')
        if set(template_fields.items()).issubset(set(input_fields.items())):
            return template.data.get('name')
    return


def type_fields(input_fields):
    typed_fields = {}

    validators = [
        (validate_date, 'date'),
        (validate_phone, 'phone'),
        (validate_email, 'email'),
    ]

    for i, value in enumerate(input_fields.values()):
        for validator, field_type in validators:
            if validator(value):
                typed_fields[f'field_name{i+1}'] = field_type
                break
        else:
            typed_fields[f'field_name{i+1}'] = 'text'

    return typed_fields


