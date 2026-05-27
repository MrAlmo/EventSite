from django.conf import settings
from django.db import models
from events.models import Event


class Registration(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='attendees'
    )
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        unique_together = ('user', 'event')
        verbose_name = 'Registration'
        verbose_name_plural = 'Registrations'

    def __str__(self):
        return f"{self.user.username} -> {self.event.title}"
