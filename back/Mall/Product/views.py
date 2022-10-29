from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


class ProductList(APIView):
    # get_전체 제품 정보
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    # post_제품 정보 추가
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)


class ProductDetail(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Http404

    # get_id로 특정 제품 찾기
    def get(self, request, format=None):
        id = request.GET['id']
        product = self.get_object(id)

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # put_특정 제품 정보 수정
    def put(self, request, format=None):
        id = request.GET['id']
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete_특정 제품 정보 삭제
    def delete(self, request, format=None):
        id = request.GET['id']
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
