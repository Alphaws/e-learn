from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from roadmap.models.user_profile import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            language="en",
            phone_number=""
        )

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()