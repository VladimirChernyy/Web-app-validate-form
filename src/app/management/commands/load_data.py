import json
import os

from django.core.management.base import BaseCommand

from app.models import TemplateFormModel
from src.settings import BASE_DIR


path = os.path.join(BASE_DIR)


class Command(BaseCommand):
    help = 'Load form templates into the database'

    def handle(self, *args, **options):
        with open(f'{path}/data/data.json', 'r') as file:
            data = json.load(file)

        for template_data in data:
            TemplateFormModel.objects.create(data=template_data)

        self.stdout.write(self.style.SUCCESS(
            'Form templates loaded successfully'
        ))
