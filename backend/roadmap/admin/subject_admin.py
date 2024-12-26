from django.contrib import admin
from parler.admin import TranslatableAdmin
from roadmap.models import Subject


@admin.register(Subject)
class SubjectAdmin(TranslatableAdmin):
    list_display = ('slug', 'title',)
