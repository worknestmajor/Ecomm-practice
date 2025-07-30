from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    name_of_category = serializers.CharField(source='category.category_name', read_only=True)
    uid = serializers.UUIDField(read_only = True)
    id = serializers.CharField(read_only = True)
    
    class Meta:
        model = Products
        fields =['id','uid','category','product_name','description','stock','price','name_of_category']
        