from django.contrib import admin
from django.utils.text import slugify
from parler.admin import TranslatableAdmin
from roadmap.models import Subject
from roadmap.models.subject import create_unique_slug


@admin.register(Subject)
class SubjectAdmin(TranslatableAdmin):
    list_display = ('slug', 'title',)
    #prepopulated_fields = {"slug": ("title",)}

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)

    get_title.short_description = 'Title'

    # def save_model(self, request, obj, form, change):
    #     print('Saving model')
    #     if not obj.slug:
    #         title = obj.safe_translation_getter('title', any_language=True) or ""
    #
    #         print('Title:',title)
    #
    #         base_slug = slugify(title)
    #         obj.slug = create_unique_slug(obj, base_slug, Subject)
    #     super().save_model(request, obj, form, change)
