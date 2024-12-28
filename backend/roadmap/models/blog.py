from django.contrib.auth.models import User
from django.db import models

class BlogPost(models.Model):
    subjects = models.ManyToManyField(
        'Subject', related_name="blog_posts"
    )
    roadmap_stages = models.ManyToManyField(
        'RoadmapStage', related_name="blog_posts", blank=True
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)  # Rövid ismertető a blogposztról
    content = models.TextField()
    language = models.CharField(
        max_length=10,
        choices=[
            ("en", "English"),
            ("hu", "Hungarian"),
            ("de", "German"),
        ],
        default="en",
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    publish_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["publish_date", "-created_at", "-updated_at", "title"]

    def __str__(self):
        return self.title

    def is_published(self):
        from django.utils.timezone import now

        return self.publish_date is not None and self.publish_date <= now()


class BlogPage(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE,
                                  related_name="pages")  # Kapcsolódás a blogbejegyzéshez
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    content = models.TextField()  # Az oldal tartalma
    sort_order = models.IntegerField(default=0)  # Az oldalak sorrendje a blogbejegyzésen belül

    class Meta:
        verbose_name = "Blog Page"
        verbose_name_plural = "Blog Pages"
        ordering = ["sort_order"]

    def __str__(self):
        return f"{self.title} (BlogPost: {self.blog_post.title})"
