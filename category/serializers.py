from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only = True)
    id = serializers.CharField(read_only = True)
    
    class Meta:
        model = Category
        fields =['id','uid','category_name','category_description']