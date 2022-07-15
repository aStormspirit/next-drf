from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework import generics

from .models import Order, Products
from .serializers import OrderSerializer, ProductSerializer


# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class Product(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class CreateOrder(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrdersList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def get_csrf(request):
    response = JsonResponse({"info": "Successfully set CSRF token"})
    response["X-CSRFToken"] = get_token(request)
    return response

