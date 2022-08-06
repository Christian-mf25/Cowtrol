from django.db import models
from uuid import uuid4


class Movement(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    move_from = models.CharField(max_length=255)
    move_to = models.CharField(max_length=255)
    days = models.IntegerField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
