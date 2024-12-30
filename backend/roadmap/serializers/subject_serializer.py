from rest_framework import serializers
from roadmap.models import Subject

class SubjectsSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ['slug', 'translations']

    def get_translations(self, obj):
        return {
            language: {
                'title': obj.safe_translation_getter('title', language_code=language),
                'description': obj.safe_translation_getter('description', language_code=language),
            }
            for language in ['hu', 'en', 'de', 'ru']
        }
