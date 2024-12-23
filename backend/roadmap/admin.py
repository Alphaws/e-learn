from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Tag, RoadmapStage, Project, Category, StageRelationship, UserProjectStatus
from django import forms
from django.urls import path
from django.shortcuts import redirect
from django.utils.html import format_html

# class RoadmapStageAdminForm(forms.ModelForm):
#     class Meta:
#         model = RoadmapStage
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
# #         self.fields['description'].widget.attrs.update({'style': 'width: 90%;'})
#         if 'translations' in self.fields:
#                     self.fields['translations'].widget.attrs.update({'style': 'width: 90%;'})


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(RoadmapStage)
class RoadmapStageAdmin(TranslatableAdmin):

    list_display = ('title','parent')
    fields = ('title', 'description')  # Mezők, amiket szerkeszthetsz

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Minden nyelvi mezőt egyszerre szerkeszthetünk
        for field in form.base_fields:
            if field.startswith('translations__'):
                form.base_fields[field].widget.attrs.update({'style': 'width: 90%;'})
        return form
#     actions = ['generate_descriptions']
#     form = RoadmapStageAdminForm
#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path(
#                 '<int:pk>/generate-description/',
#                 self.admin_site.admin_view(self.generate_description_view),
#                 name='roadmapstage_generate_description',
#             ),
#         ]
#         return custom_urls + urls
#
#     def generate_description_view(self, request, pk):
#         obj = self.get_object(request, pk)
#         if not obj:
#             self.message_user(request, "Object not found.", level='error')
#             return redirect("..")
#         # Handling translations
#         description = generate_description(obj.title)
#         obj.translations.update_or_create(language_code='en', defaults={'description': description})
#         obj.save()
#         self.message_user(request, "Description generated successfully.")
#         return redirect("..")

#     def render_change_form(self, request, context, *args, **kwargs):
#         if 'original' in context:
#             obj = context['original']
#
#             print(obj)
#             print(context['adminform'])
#
#             context['adminform'].form.fields['translations'].help_text = format_html(
#                 '<a href="{}" class="button" style="margin-top: 10px;">Generate Description</a>',
#                 f'../{obj.pk}/generate-description/'
#             )
#         return super().render_change_form(request, context, *args, **kwargs)

#     def generate_descriptions(self, request, queryset):
#         for stage in queryset:
#             # Check and generate description for translation
#             if not stage.translations.filter(language_code='en').exists():
#                 stage.translations.create(language_code='en', description=generate_description(stage.title))
#             else:
#                 stage.translations.update_or_create(language_code='en', defaults={'description': generate_description(stage.title)})
#             stage.save()
#         self.message_user(request, "Descriptions generated successfully.")
#
#     generate_descriptions.short_description = "Generate descriptions using AI"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'category')

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name',)

@admin.register(StageRelationship)
class StageRelationshipAdmin(admin.ModelAdmin):
    list_display = ('from_stage', 'to_stage', 'relationship_type')


@admin.register(UserProjectStatus)
class UserProjectStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'started', 'finished')
