from django.contrib import admin

# Register your models here.
from .models import Pedido,Linea_pedido

admin.site.register([Pedido,Linea_pedido])