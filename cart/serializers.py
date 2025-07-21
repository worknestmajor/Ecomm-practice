from rest_framework import serializers
from .models import Carts

class CartSerializer(serializers.ModelSerializer):
    p_name = serializers.CharField(source='product.product_name', read_only=True)

    class Meta:
        model = Carts
        fields = ['id', 'product', 'p_name', 'quantity']