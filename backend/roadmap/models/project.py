from django.db import models
from .tag import Tag
from django_quill.fields import QuillField

class Project(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Könnyű'),
        ('medium', 'Közepes'),
        ('hard', 'Nehéz'),
    ]

    name = models.CharField(max_length=200)
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default='medium',
    )
    short_description = models.CharField(max_length=500)
    description = QuillField()
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='projects')
    tags = models.ManyToManyField(Tag, related_name="projects")  # Címkék

    def __str__(self):
        return self.name


class UserProjectStatus(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='project_statuses')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='statuses')
    started = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    github_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.project.name}"

