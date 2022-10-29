from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerSerializer
from .models import Customer


class CustomerList(APIView):
    # get_전체 고객 정보
    def get(self, request, format=None):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    # post_고객 정보 추가
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)


class CustomerDetail(APIView):
    def get_object(self, id):
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            return Http404

    # get_id로 특정 고객 찾기
    def get(self, request, format=None):
        id = request.GET['id']
        customer = self.get_object(id)

        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    # put_특정 고객 정보 수정
    def put(self, request, format=None):
        id = request.GET['id']
        customer = self.get_object(id)
        serializer = CustomerSerializer(customer, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete_특정 고객 정보 삭제
    def delete(self, request, format=None):
        id = request.GET['id']
        customer = self.get_object(id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
