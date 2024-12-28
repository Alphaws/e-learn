from rest_framework import serializers
from roadmap.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "description", "publish_date", "language"]
