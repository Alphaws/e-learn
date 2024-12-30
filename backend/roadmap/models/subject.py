from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from parler.models import TranslatableModel, TranslatedFields


class Subject(TranslatableModel):
    slug = models.SlugField(unique=True)
    sort_order = models.IntegerField(default=0)
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        description=models.TextField(null=True, blank=True)
    )

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        ordering = ['sort_order']

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)



def create_unique_slug(instance, slug, model_class):
    unique_slug = slug
    counter = 1
    while model_class.objects.filter(slug=unique_slug).exclude(pk=instance.pk).exists():
        unique_slug = f"{slug}-{counter}"
        counter += 1
    return unique_slug



# Signal to populate slug field
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        title = instance.safe_translation_getter('title', any_language=True) or ""
        base_slug = slugify(title)
        instance.slug = create_unique_slug(instance, base_slug, sender)


pre_save.connect(create_slug, sender=Subject)
