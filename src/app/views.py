from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from core.services import find_matching_form, type_fields


class FormTemplateView(APIView):
    def post(self, request):
        input_fields = {
            key: value for (key, value) in request.query_params.items()
        }
        phone_number = input_fields.get('phone', '')
        if phone_number and not phone_number.startswith('+'):
            input_fields.update({'phone': '+' + phone_number.lstrip()})
        matching_form = find_matching_form(input_fields)
        if matching_form:
            return Response(matching_form, status=status.HTTP_200_OK)
        typed_fields = type_fields(input_fields)
        return Response(typed_fields, status=status.HTTP_200_OK)
