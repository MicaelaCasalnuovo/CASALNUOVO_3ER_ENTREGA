from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from App.models import Cliente
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

def Cliente_formulario(request):
    if request.method == 'POST':
        cliente = Cliente(
            nombre=request.POST.get('nombre'),  
            apellido=request.POST.get('apellido'),  
            dni=request.POST.get('dni')  
        )
        cliente.save()
        
        return redirect('App/Cliente.html')  # Redirige a la página de clientes después de guardar
    
    return render(request, 'App/cliente_formulario.html')
