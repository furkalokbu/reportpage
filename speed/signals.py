from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from speed.models import UserData
from core.utils import generate_random_string

@receiver(pre_save, sender=UserData)
def add_slug_to_user_data(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.date)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string

