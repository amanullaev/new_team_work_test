from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    CHOICES = (
        (1, 'admin'),
        (2, 'user')
    )
    roles = models.PositiveSmallIntegerField(default=2, choices=CHOICES)