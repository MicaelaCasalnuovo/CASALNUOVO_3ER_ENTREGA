from django.urls import path
from . import views 

urlpatterns = [
    path('Inicio/', views.Inicio, name="Inicio"),
    path('Cliente/', views.Cliente, name="Cliente"),
    path('Sku/', views.Sku, name="Sku"),
    path('Stock/', views.Stock, name="Stock"),
    path('Factura/', views.Factura, name="Factura"),
]