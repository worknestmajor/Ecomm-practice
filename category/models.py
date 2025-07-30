from django.db import models
# from base.manager import BaseManager
from base.models import BaseModel

# Create your models here.
class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name