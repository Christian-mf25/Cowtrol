from django.db import models
from uuid import uuid4


class Movement(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    days = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
