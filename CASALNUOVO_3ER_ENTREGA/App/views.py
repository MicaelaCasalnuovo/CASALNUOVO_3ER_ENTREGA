from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Cliente(request) :
    return HttpResponse ("Vista Cliente")

def Sku(request) :
    return HttpResponse ("Vista Sku")

def Stock(request) :
    return HttpResponse ("Vista Stock")

def Factura(request) :
    return HttpResponse ("Vista factura")