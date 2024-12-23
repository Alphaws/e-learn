from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=10, choices=[
        ('en', 'English'),
        ('hu', 'Hungarian'),
        ('de', 'German'),
        # Add more languages as needed
    ])
    phone_number = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.name
