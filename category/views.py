from django.shortcuts import render
from .serializers import CategorySerializer
from .models import Category
from base.views import BaseView
from base.permissions import IsSuperUser
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CategoryView(BaseView):
    model = Category
    serializer_class= CategorySerializer
