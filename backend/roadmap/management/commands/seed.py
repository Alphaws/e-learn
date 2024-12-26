from django.core.management.base import BaseCommand, CommandError

from roadmap.models import Tag, RoadmapStage, StageRelationship, Roadmap
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **kwargs):
        tags = [
            "API",
            "CSS",
            "Django",
            "Flask",
            "Frameworks",
            "Frontend",
            "HTML",
            "JavaScript",
            "MongoDB",
            "Php",
            "PostgreSQL",
            "Psycopg2",
            "Python",
            "SQLAlchemy",
            "Web Development",
        ]

        for name in tags:
            tag, created = Tag.objects.get_or_create(
                name=name,
                slug=slugify(name)
            )
            if created:
                self.stdout.write(f'Tag created: {tag.name}')
            else:
                self.stdout.write(f'Tag already exists: {tag.name}')

        # @todo: data.json feldolgozása

        self.stdout.write(self.style.SUCCESS('Database successfully seeded!'))
