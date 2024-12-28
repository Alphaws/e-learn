from django.core.management.base import BaseCommand, CommandError

from roadmap.models import Tag, RoadmapStage, StageRelationship, Roadmap, Subject
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
        subjects_data = [
            {
                "slug": "matek",
                "sort_order": 1,
                "title": {
                    "en": "Math",
                    "hu": "Matematika",
                    "de": "Mathe"
                },
                "description": {
                    "en": "Mathematics is present in all areas of life. Learn the basics and advanced concepts!",
                    "hu": "A matematika az élet minden területén jelen van. Ismerd meg az alapokat és haladó fogalmakat!",
                    "de": "Mathematik ist in allen Lebensbereichen präsent. Lernen Sie die Grundlagen und fortgeschrittenen Konzepte!"
                }
            },
            {
                "slug": "fizika",
                "sort_order": 2,
                "title": {
                    "hu": "Fizika",
                    "en": "Physics",
                    "de": "Physik"
                },
                "description": {
                    "hu": "Fedezd fel a természet törvényeit és a világegyetem működését.",
                    "en": "Discover the laws of nature and how the universe works.",
                    "de": "Entdecken Sie die Naturgesetze und wie das Universum funktioniert."
                }
            },
            {
                "slug": "kemia",
                "sort_order": 3,
                "title": {
                    "hu": "Kémia",
                    "en": "Chemistry",
                    "de": "Chemie"
                },
                "description": {
                    "hu": "Tanulj a kémiai anyagokról, reakciókról és a kémia szépségeiről.",
                    "en": "Learn about chemical substances, reactions, and the beauty of chemistry.",
                    "de": "Erfahren Sie mehr über Chemikalien, Reaktionen und die Schönheit der Chemie."
                }
            },
            {
                "slug": "info",
                "sort_order": 4,
                "title": {
                    "hu": "Informatika",
                    "en": "Information Technology",
                    "de": "Informations-Technik"
                },
                "description": {
                    "hu": "Merülj el az informatika világában a számítógépek működésétől a programozásig.",
                    "en": "Immerse yourself in the world of IT, from how computers work to programming.",
                    "de": "Tauchen Sie ein in die Welt der IT, von der Funktionsweise von Computern bis zur Programmierung."
                }
            },

        ]
        for subject_data in subjects_data:
            subject, created = Subject.objects.get_or_create(
                slug=subject_data['slug'],
                sort_order=subject_data['sort_order']
            )
            for lang_code, title in subject_data['title'].items():
                subject.set_current_language(lang_code)
                subject.title = title
                subject.description = subject_data['description'].get(lang_code, "")

                # Mentés
            subject.save()

            if created:
                self.stdout.write(f'Subject created: {subject.title}')
            else:
                self.stdout.write(f'Subject already exists: {subject.title}')

        courses = [{
            "slug": "elso-matek-oram",
            "title": {
                "en": "First Math Course",
                "hu": "",
                "de": ""
            },
            "description": {},
        }
        ]

        self.stdout.write(self.style.SUCCESS('Database successfully seeded!'))
