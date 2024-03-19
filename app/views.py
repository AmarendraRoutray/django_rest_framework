from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class ProductCrud(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductModelSerializer