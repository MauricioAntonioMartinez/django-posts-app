from django.contrib.auth.models import User
from django.db.models.signals import post_save  # fiered after a model is saved
from django.dispatch import receiver

from .models import Profile


# signal and sender // when a user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kargs):
    if created:
        Profile.objects.create(user=instance)  # create upon a user is created


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kargs):
    instance.profile.save()
