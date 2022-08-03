from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

class Farm(AbstractUser):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	name = models.CharField(max_length=255, unique=True)

	USERNAME_FIELD = "name"
