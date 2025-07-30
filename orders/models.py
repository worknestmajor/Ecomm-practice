from django.db import models
from base.models import BaseModel
from accounts.models import Account
# from base.manager import BaseManager
from product.models import Products


# Create your models here.
class Order(BaseModel):
    user = models.ForeignKey(Account, on_delete= models.CASCADE)
    address = models.CharField(max_length=255)
    total_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField() 

    def __str__(self):
        return self.product.product_name