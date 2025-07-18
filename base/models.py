from django.db import models
from .manager import BaseManager
import uuid
# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    objects = BaseManager()

    class Meta:
        abstract = True
