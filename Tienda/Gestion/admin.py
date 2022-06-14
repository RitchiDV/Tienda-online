from django.contrib import admin
from Gestion.models import Clientes,Articulos,pedidos#importado del modulo models


# Register your models here.



class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","email","tfno")
    search_fields=("nombre","tfno")


class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre","seccion","precio")
    search_fields=("nombre","seccion",)
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado",)
    list_filter=("fecha",)
    date_hierarchy="fecha" #detecta todos los meses de cada pedido 




admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Articulos,ArticulosAdmin)
admin.site.register(pedidos,PedidosAdmin) 