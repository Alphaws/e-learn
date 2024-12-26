from django.contrib import admin
from roadmap.models import Course, Chapter, Lesson, Media
from parler.admin import TranslatableAdmin


@admin.register(Course)
class CourseAdmin(TranslatableAdmin):
    list_display = ('slug', 'get_title', 'level')

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)

    get_title.short_description = 'Title'


@admin.register(Chapter)
class ChapterAdmin(TranslatableAdmin):
    list_display = ('course', 'get_title', 'sort_order')

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)

    get_title.short_description = 'Title'


@admin.register(Lesson)
class LessonAdmin(TranslatableAdmin):
    list_display = ('chapter', 'get_title', 'lesson_type')

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)

    get_title.short_description = 'Title'


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('media_type', 'lesson', 'file', 'url')
