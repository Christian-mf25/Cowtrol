from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4


class Area(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    area_name = models.CharField(unique=True, max_length=255)
    limit_space = models.IntegerField()
    free_space = models.IntegerField(default=limit_space)
    occupied_space = models.IntegerField(default=0)
    gmd = models.DecimalField(max_digits=12, decimal_places=2)

    farm = models.ForeignKey("farms.Farm", on_delete=CASCADE, related_name="areas")
