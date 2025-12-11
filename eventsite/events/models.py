from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.urls import reverse



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    max_attendance = models.IntegerField(default=0, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})