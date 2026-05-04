import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomWorker(AbstractUser):
    """Object representing a co-worker."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        """Return the internal representation for print statements."""
        return self.username
