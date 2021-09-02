from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class UserData(models.Model):

    date = models.DateField(_("date"))
    distance = models.FloatField(_("distance"))
    duration = models.FloatField(_("duration"))
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=CASCADE,
                            related_name="user",
                             null=True, blank=True
                            )

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        ordering = ("updated_at",)
        verbose_name = _("data user")
    
    def __str__(self):
        return self.slug

class SpeedUserData(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=CASCADE,
                            related_name="speed",
                                null=True, blank=True
                            )
    average_speed = models.FloatField(_("average_speed"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        verbose_name = _("speed")
    
    def __str__(self):
        return str(self.user)
