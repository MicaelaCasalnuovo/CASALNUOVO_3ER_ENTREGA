from django.contrib import admin
from App.models import Cliente
from App.models import Stock
from App.models import Sku
from App.models import Factura

# Register your models here.
admin.site.register (Cliente)
admin.site.register (Stock)
admin.site.register (Sku)
admin.site.register (Factura)