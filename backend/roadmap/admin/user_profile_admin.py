from django.contrib import admin

from roadmap.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'phone_number', 'language', 'avatar')

    def user_email(self, obj):
        """
        Access the related User's email field.
        """
        return obj.user.email

    user_email.short_description = 'Email'  # Label for the list header
