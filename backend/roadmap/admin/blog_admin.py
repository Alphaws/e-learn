from django.contrib import admin
from roadmap.models import Subject, BlogPost, BlogPage


class PageInline(admin.TabularInline):
    model = BlogPage
    extra = 1


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    inlines = [PageInline]
