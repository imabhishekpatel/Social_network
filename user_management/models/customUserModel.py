from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)

    class Meta:
        verbose_name = 'User'       
        db_table = "custome_user"

