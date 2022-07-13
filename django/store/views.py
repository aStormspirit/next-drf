from django.shortcuts import render
from rest_framework import generics

from .models import Products
from .serializers import ProductSerializer


# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class Product(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
