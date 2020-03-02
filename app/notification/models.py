from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# Create your models here.
class Notifications(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    notif = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(Notifications, self).save(force_insert, force_update, using, update_fields)
        channel_layer = get_channel_layer()
        print(channel_layer)
        async_to_sync(channel_layer.group_send)(
            'infochannel',
            {
                'type': 'infochannel_message',
                'notif': self.notif
            }
        )


@receiver(post_save, sender=User)
def create_notification(sender, instance, created, **kwargs):
    if created:
        notif = Notifications()
        notif.sender = instance
        notif.notif = "user " + instance.username + " added in model"
        notif.save()


