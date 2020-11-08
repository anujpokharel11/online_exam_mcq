from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_client = models.BooleanField(default=True)


