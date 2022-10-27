from django.shortcuts import render
from rest_framework import viewsets, mixins
from .serializers import OrderSerializer, OrderListSerializer
from .models import Order
from django_filters.rest_framework import DateFromToRangeFilter, DjangoFilterBackend, FilterSet
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
