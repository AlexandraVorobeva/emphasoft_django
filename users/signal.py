from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile_of_user


@receiver(post_save, sender=Profile_of_user)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile_of_user.objects.create(user=instance)