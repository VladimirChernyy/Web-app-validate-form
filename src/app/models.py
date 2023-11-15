from django.db import models


class TemplateFormModel(models.Model):
    data = models.JSONField(db_index=True)

    def __str__(self):
        return str(self.id)
