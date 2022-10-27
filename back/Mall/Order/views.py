from urllib import request
from django.shortcuts import render
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DateFromToRangeFilter, DjangoFilterBackend, FilterSet
from rest_framework.decorators import action
from .serializers import OrderSerializer, OrderListSerializer
from .models import Order

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
    serializer_class = OrderListSerializer

    def get_queryset(self):
        date = self.request.query_params.get('date')

        if date:
            queryset = Order.objects.filter(ordered_at__startswith=date)
        return queryset
