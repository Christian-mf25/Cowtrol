from tkinter import CASCADE
from django.db import models
from uuid import uuid4


class Area(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    area_name = models.CharField(max_length=255)
    limit_space = models.IntegerField()
    free_space = models.IntegerField()
    occupied_space = models.IntegerField(default=0)
    gmd = models.DecimalField(max_digits=3, decimal_places=2)

    farm = models.ForeignKey(
		"farms.Farm", on_delete=models.CASCADE, related_name="areas"
		)
