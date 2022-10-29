from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_name", "price"]
