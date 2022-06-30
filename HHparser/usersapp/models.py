from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ParserUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_author = models.BooleanField(default=False)
