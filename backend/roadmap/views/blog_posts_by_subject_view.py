from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from roadmap.models import BlogPost
from roadmap.serializers import BlogPostSerializer


class BlogPostsBySubjectView(ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]  # Bárki hozzáférhet
    lookup_url_kwarg = "subject_slug"  # A URL-ben található slug (például "programming-basics")

    def get_queryset(self):
        """
        Csak a megadott tantárgyhoz kapcsolódó blogbejegyzéseket listázza.
        """
        subject_slug = self.kwargs.get(self.lookup_url_kwarg)
        return BlogPost.objects.filter(subjects__slug=subject_slug).distinct()
