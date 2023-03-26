from django.urls import path
from django.contrib import admin
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('products.urls')),
    path('view/', include('view.urls')),
    path('payments/', include('payments.urls')),
]


