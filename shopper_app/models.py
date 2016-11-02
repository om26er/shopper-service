from django.db import models

from simple_login.models import BaseUser


class User(BaseUser):
    full_name = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=2000, blank=False)
    province = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=255, blank=False)
