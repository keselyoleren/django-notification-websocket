from django.db.models.signals import post_save
from notification.models import Notifications
from django.dispatch import receiver
from django.contrib.auth.models import User
from datetime import datetime

@receiver(post_save, sender=User)
def create_notification(sender, instance, created, **kwargs):
    print('examlpe')
    if created:
        notif = Notifications
        notif.user = instance
        notif.notif = "user" + instance.username + "added in model"
        notif.save()

