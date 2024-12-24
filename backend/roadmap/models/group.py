from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class Group(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100)
    )
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_groups')

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
