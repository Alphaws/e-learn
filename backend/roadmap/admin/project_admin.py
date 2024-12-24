from django.contrib import admin
from roadmap.models import Project, UserProjectStatus


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'category')
    class Media:
        css = {
            "all": "css/custom_admin.css"
        }


@admin.register(UserProjectStatus)
class UserProjectStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'started', 'finished')

