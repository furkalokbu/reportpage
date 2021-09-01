from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from speed.models import UserData
from speed.models import SpeedUserData
from core.utils import generate_random_string

from core.average_speed import AverageSpeed


@receiver(pre_save, sender=UserData)
def add_slug_to_user_data(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.date)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string

        data_list = []
        data_user = UserData.objects.filter(user=instance.user).values_list('distance', 'duration')
        
        for item in data_user:
            data_list.append(item)
        
        tools = AverageSpeed()
        print(data_list)
        print(tools.speed(data_list))
