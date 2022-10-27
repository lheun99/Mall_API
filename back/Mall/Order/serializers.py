from rest_framework import serializers
from .models import Order
from Customer.serializers import CustomerInfoSerializer
from Product.serializers import ProductInfoSerializer
from phonenumber_field.serializerfields import PhoneNumberField


# 주문서 정보
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderListSerializer(serializers.ModelSerializer):
    orderer_info = serializers.SerializerMethodField()
    product_info = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    recipient_phone_number = PhoneNumberField(region="SK")

    class Meta:
        model = Order
        fields = ["id",
                  "ordered_at",
                  "orderer_info",
                  "product_info",
                  "quantity",
                  "recipient_name",
                  "recipient_phone_number",
                  "address",
                  "status"]

    # 주문자 정보 구성
    def get_orderer_info(self, instance):
        order_info = CustomerInfoSerializer(instance.orderer_id).data
        return order_info

    # 제품 정보 구성
    def get_product_info(self, instance):
        product_info = ProductInfoSerializer(instance.product_id).data
        return product_info

    # 주문서 상태 구성
    def get_status(self, instance):
        status = instance.get_status_display()
        return status
