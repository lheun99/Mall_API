from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('Customer.urls')),
    path('product/', include('Product.urls')),
    path('order/', include('Order.urls')),

]
