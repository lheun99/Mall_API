from urllib import request
from django.shortcuts import render
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DateFromToRangeFilter, DjangoFilterBackend, FilterSet
from rest_framework.decorators import action
from .serializers import OrderDataSerializer, OrderSerializer, OrderListSerializer
from .models import Order
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models import F
# Create your views here.


class OrderFilter(FilterSet):
    ordered_at = DateFromToRangeFilter()

    class Meta:
        model = Order
        fields = ['orderer_id', 'status', 'ordered_at']


class OrderViewSet(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter


class OrderDataViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = OrderDataSerializer

    def list(self, request, *args, **kwargs):
        date = self.request.query_params.get('date')
        queryset = Order.objects.filter(ordered_at__startswith=date).select_related().values(
            'quantity', 'product_id__price').annotate(total=F('quantity')*F('product_id__price')).aggregate(Sum('total'))
        serializer = self.get_serializer_class()
        return Response(serializer(queryset).data)
