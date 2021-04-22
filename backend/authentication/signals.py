import os
from django.db.models.signals import post_save
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.dispatch import receiver
from django.utils import timezone
from io import BytesIO


from authentication.models import CoreUser
from api.models import Employee

@receiver(post_save, sender=CoreUser)
def create_user(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        user = Employee.objects.create(
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            
        )
        user.save()
        instance.user = user
        instance.save()
