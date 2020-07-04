from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    wallet = models.FloatField(default=10000.00)
