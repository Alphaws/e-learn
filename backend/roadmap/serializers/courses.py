from rest_framework import serializers
from roadmap.models import Course, Prerequisite

class PrerequisiteSerializer(serializers.ModelSerializer):
    prerequisite_type = serializers.SerializerMethodField()
    prerequisite_slug = serializers.SerializerMethodField()

    class Meta:
        model = Prerequisite
        fields = ['prerequisite_type', 'prerequisite_slug']

    def get_prerequisite_type(self, obj):
        return obj.content_type.model

    def get_prerequisite_slug(self, obj):
        return obj.prerequisite.slug if hasattr(obj.prerequisite, 'slug') else None

class CourseSerializer(serializers.ModelSerializer):
    prerequisites = PrerequisiteSerializer(many=True, read_only=True)
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
            for language in ['hu', 'en', 'de']  # Add supported languages here
        }
