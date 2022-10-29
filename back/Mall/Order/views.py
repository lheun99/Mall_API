from django.shortcuts import render
from django_filters.rest_framework import DateFromToRangeFilter, DjangoFilterBackend, FilterSet
from django.db.models import Sum, Count, F
from django.db.models.functions import TruncDate

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import OrderDataSerializer, OrderSerializer, OrderListSerializer
from .models import Order


class OrderFilter(FilterSet):
    ordered_at = DateFromToRangeFilter()

    class Meta:
        model = Order
        fields = ['orderer_id', 'status', 'ordered_at']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter


class OrderDataViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = OrderDataSerializer

    @action(detail=False)
    def total_sales(self, request, *args, **kwargs):
        queryset = Order.objects.select_related().annotate(
            date=TruncDate('ordered_at')).values('date').annotate(total=Sum(F('quantity')*F('product_id__price'))).order_by('date')
        serializer = self.get_serializer_class()
        return Response(serializer(queryset).data)

    @action(detail=False)
    def sales_quantity(self, request, *args, **kwargs):
        queryset = Order.objects.select_related().annotate(
            date=TruncDate('ordered_at')).values('date').annotate(quantity=Count('quantity'), product=F('product_id__product_name')).values('date', 'product', 'quantity').order_by('date')
        serializer = self.get_serializer_class()
        return Response(serializer(queryset).data)

    @ action(detail=False)
    def sales_price(self, request, *args, **kwargs):
        queryset = Order.objects.select_related().annotate(
            date=TruncDate('ordered_at')).values('date').annotate(price=Sum('product_id__price'), product=F('product_id__product_name')).values('date', 'product', 'price').order_by('date')
        serializer = self.get_serializer_class()
        return Response(serializer(queryset).data)
