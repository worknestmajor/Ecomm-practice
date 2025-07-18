from django.shortcuts import render
from .serializers import CategorySerializer
from .models import Category
from base.views import BaseView
# Create your views here.

class CategoryView(BaseView):
    model = Category
    serializer_class= CategorySerializer
