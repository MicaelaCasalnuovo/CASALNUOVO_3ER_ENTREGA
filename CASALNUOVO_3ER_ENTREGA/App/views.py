from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Inicio(request) :
    return render (request, "App/Inicio.html")

def Cliente(request) :
    return render (request, "App/Cliente.html")

def Sku(request) :
    return render (request, "App/Sku.html")

def Stock(request) :
    return render (request, "App/Stock.html")

def Factura(request) :
    return render (request, "App/Factura.html")
