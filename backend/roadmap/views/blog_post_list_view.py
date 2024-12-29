from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from roadmap.models import BlogPost
from roadmap.serializers import BlogPostSerializer

class BlogPostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class BlogPostListView(ListAPIView):
    # queryset = BlogPost.objects.filter(published=True).order_by('-created_at')
    serializer_class = BlogPostSerializer
    pagination_class = BlogPostPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']  # Allow searching by title and content
    ordering_fields = ['created_at', 'title']

    def get_queryset(self):
        """
        Return all blog posts if the user is a superuser.
        Otherwise, apply the filter for non-superuser users.
        """
        user = self.request.user
        if user.is_superuser:  # If the user is a superuser, return all posts
            return BlogPost.objects.all().order_by('-created_at')
        # Otherwise, filter for published posts only
        return BlogPost.objects.filter(publish_date__isnull=False).order_by('-created_at')
