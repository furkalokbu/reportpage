from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class UserData(models.Model):

    date = models.DateField()
    distance = models.FloatField(_("distance"))
    duration = models.FloatField(_("duration"))
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=CASCADE,
                            related_name="user"
                            )

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.slug