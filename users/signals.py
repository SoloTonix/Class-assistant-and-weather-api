from django.dispatch import receiver
from.models import *
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def update_profile(sender, created, instance, **kwargs):
    if created == False:
        profile = Profile.objects.filter(user=instance)
        




