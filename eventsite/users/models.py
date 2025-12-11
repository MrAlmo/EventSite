from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(null=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    is_moderator = models.BooleanField(
        default=False,
        help_text='User is moderator or not.'
    )

    def __str__(self):
        return self.username
