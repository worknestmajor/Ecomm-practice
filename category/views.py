from django.shortcuts import render
from .serializers import CategorySerializer
from .models import Category
from base.views import BaseView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
# from base.permissions import IsAdmin,IsStaffWithLimitedAccess
# from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CategoryView(BaseView):
    model = Category
    serializer_class= CategorySerializer

