from django.db import models
from base.models import BaseModel
# from base.manager import BaseManager
from accounts.models import Account
from product.models import Products
# Create your models here.

class Carts(BaseModel):
    user = models.ForeignKey(Account, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

