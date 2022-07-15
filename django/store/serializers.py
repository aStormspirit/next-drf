from rest_framework import serializers

from .models import Order, Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
