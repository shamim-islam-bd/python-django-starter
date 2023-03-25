from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def payments(request):
    return render(request, 'payments-1.html', {})

def payments2(request):
    return render(request, 'payments-2.html', {})