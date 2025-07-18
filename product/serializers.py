from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.category_name', read_only=True)
    class Meta:
        model = Products
        fields ='__all__'