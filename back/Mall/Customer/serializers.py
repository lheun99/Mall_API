from rest_framework import serializers
from .models import Customer
from phonenumber_field.serializerfields import PhoneNumberField


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerInfoSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(region="SK")

    class Meta:
        model = Customer
        fields = ["customer_name", "phone_number"]
