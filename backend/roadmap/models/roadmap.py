from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django_quill.fields import QuillField
from .subject import Subject


class Roadmap(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        description=QuillField(),
    )
    start_stage = models.ForeignKey(
        'RoadmapStage',
        on_delete=models.CASCADE,
        related_name='roadmap_start_stage'
    )
    subjects = models.ManyToManyField(
        Subject,
        related_name='roadmaps'
    )

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)


class RoadmapStage(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        description=QuillField(null=True, blank=True),
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_stages'
    )

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)


class StageRelationship(models.Model):
    from_stage = models.ForeignKey(
        RoadmapStage, on_delete=models.CASCADE, related_name='outgoing_relationships'
    )
    to_stage = models.ForeignKey(
        RoadmapStage, on_delete=models.CASCADE, related_name='incoming_relationships'
    )
    relationship_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.from_stage} -> {self.to_stage} ({self.relationship_type})"
