from rest_framework.generics import RetrieveAPIView

from roadmap.models import BlogPost
from roadmap.serializers import BlogPostSerializer


class BlogPostRetrieveView(RetrieveAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
    lookup_field = 'slug'
