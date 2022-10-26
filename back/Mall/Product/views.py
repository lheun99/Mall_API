from django.shortcuts import render, HttpResponse
from .models import Product
# Create your views here.


def create(request):
    product = Product(
        product_name="제품1",
        price=10000

    )
    print(product)
    product.save()

    return HttpResponse("제품 생성")
