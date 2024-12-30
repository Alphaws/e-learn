from rest_framework import serializers
from roadmap.models import Course


class CourseSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['slug', 'level', 'tags', 'translations', 'prerequisites']

    def get_translations(self, obj):
        return {
            language: {
                'title': obj.safe_translation_getter('title', language_code=language),
                'description': obj.safe_translation_getter('description', language_code=language)
            }
            for language in ['hu', 'en', 'de']
        }
