from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from parler.models import TranslatableModel, TranslatedFields


class Course(TranslatableModel):
    slug = models.SlugField(unique=True)
    level = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    tags = models.TextField(help_text="Comma-separated tags")
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        description=models.TextField(null=True, blank=True)
    )


    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or self.slug


class Chapter(TranslatableModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='chapters')
    sort_order = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        description=models.TextField(null=True, blank=True)
    )


    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"
        ordering = ['sort_order']

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)


class Lesson(TranslatableModel):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='lessons')
    sort_order = models.IntegerField(default=0)
    lesson_type = models.CharField(max_length=50, choices=[
        ('text', 'Text'),
        ('video', 'Video'),
    ])
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        description=models.TextField(null=True, blank=True)
    )
    video_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        ordering = ['sort_order']

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or f"Lesson {self.sort_order}"


class Media(models.Model):
    MEDIA_TYPES = [
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('link', 'Link'),
        ('image', 'Image'),
        ('document', 'Document'),
    ]

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='media')
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES)
    title = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='lesson_media/', null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"

    def __str__(self):
        title = self.title or "Untitled"
        media_type = self.media_type or "Unknown"
        media_reference = self.file or self.url or "No media"
        return f"{title} ({media_type}): {media_reference}"


"""
lesson = Lesson.objects.get(id=1)

# Add audio
audio = Media.objects.create(
    lesson=lesson,
    media_type='audio',
    file='path/to/audio.mp3'
)

# Add a YouTube link
video = Media.objects.create(
    lesson=lesson,
    media_type='video',
    url='https://youtube.com/example'
)


lesson = Lesson.objects.get(id=1)
media_items = lesson.media.all()

for media in media_items:
    print(media.media_type, media.file or media.url)

"""