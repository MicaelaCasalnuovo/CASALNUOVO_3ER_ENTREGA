
from django.urls import path
from App import views

urlpatterns = [
    path('Inicio/', views.Inicio),
    path('Cliente/', views.Cliente),
    path('Sku/', views.Sku),
    path('Stock/', views.Stock),
    path('Factura/', views.Factura),
]
