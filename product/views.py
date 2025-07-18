from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Products
from rest_framework.response import Response

from base.views import BaseView
# Create your views here.

class ProductView(BaseView):
    model = Products
    serializer_class = ProductSerializer


