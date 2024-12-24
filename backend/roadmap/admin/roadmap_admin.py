from django.contrib import admin
from parler.admin import TranslatableAdmin
from roadmap.models import Roadmap

@admin.register(Roadmap)
class RoadmapAdmin(TranslatableAdmin):
    list_display = ('title',)