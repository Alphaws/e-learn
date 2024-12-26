from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Prerequisite(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    prerequisite = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.content_type.model} - {self.prerequisite}"
