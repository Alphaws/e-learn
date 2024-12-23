from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class Roadmap(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        description=models.TextField(null=True, blank=True),
    )
    start_stage = models.ForeignKey('RoadmapStage', on_delete=models.CASCADE, related_name='roadmap_start_stage')

class RoadmapStage(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        description=models.TextField(null=True, blank=True),
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

