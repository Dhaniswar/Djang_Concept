from django.db.models.signals import post_save
from django.dispatch import receiver
from firebase_admin import db

from .models import UserSetting


@receiver(post_save, sender=UserSetting)
def save_profession(sender, instance, **kwargs):
    print(" Instance data => ", instance.data)
    ref = db.reference(f'/users2/{str(instance.uuid)}/userSettings/')
    ref.update(instance.data)

