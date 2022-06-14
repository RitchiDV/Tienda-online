from django.shortcuts import render
from pedidos.models import Pedido

# Create your views here.
def pedidos (request):
    pedido=Pedido.objects.all()

     
    return render(request,"pedidos/pedidos.html",{"pedido":pedido})
