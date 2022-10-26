from django.shortcuts import render, HttpResponse
from django.core import serializers
from .models import Customer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json


@csrf_exempt
def create_customer(request):
    data = json.loads(request.body)

    if request.method == 'POST':
        customer = Customer()

        customer.email = data['email']
        customer.customer_name = data['customer_name']
        customer.phone_number = data['phone_number']

    customer.save()
    return HttpResponse(customer)


def customer_list(request):
    customers = serializers.serialize("json", Customer.objects.all())
    return HttpResponse(customers)
