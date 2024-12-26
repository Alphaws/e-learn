from django.contrib import admin
from roadmap.models import Course, Chapter, Lesson, Media


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('media_type', 'lesson', 'file', 'url')
