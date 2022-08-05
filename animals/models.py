from django.db import models

from uuid import uuid4


class Animal(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    owner_id = models.CharField(max_length=255)

    area = models.ForeignKey(
        "areas.Area", on_delete=models.CASCADE, related_name="animals"
    )

    movement = models.ForeignKey(
        "movements.Movement", on_delete=models.CASCADE, related_name="animals", null=True
    )
