from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=250, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
