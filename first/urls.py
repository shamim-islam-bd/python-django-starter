from django.urls import path
from django.contrib import admin
from django.urls.conf import include

urlpatterns = [
    path('product/', include('products.urls')),
    path('view/', include('view.urls')),
    path('payments/', include('payments.urls')),
]


