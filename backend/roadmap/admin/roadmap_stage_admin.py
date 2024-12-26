from django.contrib import admin
from parler.admin import TranslatableAdmin

from roadmap.models import RoadmapStage, StageRelationship


@admin.register(RoadmapStage)
class RoadmapStageAdmin(TranslatableAdmin):
    list_display = ('title', 'parent')
    fields = ('title', 'description', 'parent')


@admin.register(StageRelationship)
class StageRelationshipAdmin(admin.ModelAdmin):
    list_display = ('from_stage', 'to_stage', 'relationship_type')
