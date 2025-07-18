from django.db import models
from base.manager import BaseManager
from base.models import BaseModel
from category.models import Category

# Create your models here.
class Products(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    stock = models.IntegerField()

    objects = BaseManager()

