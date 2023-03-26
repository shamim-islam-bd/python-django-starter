from django.shortcuts import render
from payments.models import pay_method

# Create your views here.
def payments(request):
    return render(request, 'payments/payments-1.html', {})

def payments2(request):
    return render(request, 'payments/payments-2.html', {})

def payment_method(request):
    pay_m = pay_method.objects.all()
    return render(request, 'payments/pay.html', {'pay': pay_m})