#Post save signal 
from django.db.models.signals import post_save

#Sender
from django.contrib.auth.models import User

#Receiver
from django.dispatch import receiver

from .models import Profile

#Create profile function. Tie receiver with decorator
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

#kwargs = keyword args
@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()