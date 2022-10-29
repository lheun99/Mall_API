from django.urls import include, path
from rest_framework import routers
from .views import OrderViewSet, OrderListViewSet, OrderDataViewSet

router = routers.DefaultRouter()
router.register(r'list', OrderListViewSet, basename='OrderList')
router.register(r'', OrderViewSet, basename='Order')
router.register(r'data', OrderDataViewSet, basename='OrderData')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
