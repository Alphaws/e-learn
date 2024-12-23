from django.contrib import admin
from parler.admin import TranslatableAdmin
from roadmap.models import Category


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name',)
