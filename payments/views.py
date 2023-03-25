from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePage(show):
    return HttpResponse('<h1>Welcome to django!</h1>')