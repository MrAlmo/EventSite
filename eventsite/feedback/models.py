from django.conf import settings
from django.db import models
from events.models import Event


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='feedbacks')
    comment = models.TextField(verbose_name='Your feedback')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name='Score (1-5)')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return f"Feedback from {self.user.username} about {self.event.title}"