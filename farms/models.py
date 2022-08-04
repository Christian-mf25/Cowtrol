from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from uuid import uuid4

class FarmManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, name, **kwargs):
        
        if not email:
            raise ValueError('The given email must set')
        email = self.normalize_email(email)
        farm = self.model(
            email=email,
            name=name,
            **kwargs
        )
        farm.set_password(password)
        farm.save(using=self._db)
        return farm

    def create_user(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        
        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        
        return self._create_user(email, password, **kwargs)


class Farm(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = FarmManager()