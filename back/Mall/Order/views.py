from itertools import product
from django.shortcuts import render, HttpResponse
from .models import Order
from Customer.models import Customer
from Product.models import Product
# Create your views here.


def create(request):
    order = Order(
        address="아파트",

        orderer=Customer.objects.get(id=1),
        product=Product.objects.get(id=1),
        quantity=1,

        recipient_name="수령자",
        recipient_phone_number='01012345678',
    )
    print(order)
    order.save()

    return HttpResponse("주문완료")


def list(request):
    return HttpResponse(Order.objects.all())
