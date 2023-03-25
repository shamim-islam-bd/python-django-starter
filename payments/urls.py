from django.urls import path
from . import views

urlpatterns = [
    path('', views.payments),
    path('pay2/', views.payments2),
]
