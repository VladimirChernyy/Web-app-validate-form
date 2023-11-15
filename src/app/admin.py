from django.contrib import admin
from app.models import TemplateFormModel


@admin.register(TemplateFormModel)
class TemplateFormAdmin(admin.ModelAdmin):
    pass
