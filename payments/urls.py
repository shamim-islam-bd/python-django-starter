from django.urls import path
from . import views

urlpatterns = [
    path('', views.payments, name='payments-1'),
    path('pay2/', views.payments2, name='payments-2'),
    path('pay/', views.payment_method, name='pay'),
]
