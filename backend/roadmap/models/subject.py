from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class Subject(TranslatableModel):
    slug = models.SlugField(unique=True)
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        description=models.TextField(null=True, blank=True)
    )
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)
