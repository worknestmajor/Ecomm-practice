from django.db import models
from base.manager import BaseManager
from base.models import BaseModel
from category.models import Category
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Products(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.IntegerField()
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    objects = BaseManager()

