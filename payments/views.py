from django.shortcuts import render

# Create your views here.
def payments(request):
    return render(request, 'payments/payments-1.html', {})

def payments2(request):
    return render(request, 'payments/payments-2.html', {})