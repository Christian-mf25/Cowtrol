from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4


class Area(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    area_name = models.CharField(unique=True, max_length=255)
    animal_limit = models.IntegerField()
    gmd = models.DecimalField(max_digits=12, decimal_places=2)
