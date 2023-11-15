from rest_framework import serializers

from app.models import TemplateFormModel
from core.validators import (
    validate_date,
    validate_email,
    validate_phone
)


class FormTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateFormModel
        fields = ('data',)

    def validate(self, data):
        validation_functions = {
            'email': (validate_email, 'Invalid email'),
            'phone': (validate_phone, 'Invalid phone'),
            'date': (validate_date, 'Invalid date'),
        }

        for field_name, field_value in data.items():
            if field_name in validation_functions:
                validation_function, error_message = validation_functions[
                    field_name]
                if not validation_function(field_value):
                    raise serializers.ValidationError(error_message)
        return data
