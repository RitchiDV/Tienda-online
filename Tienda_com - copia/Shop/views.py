from django.shortcuts import render
from Shop.models import CategoriaP,Producto

# Create your views here.
def shop(request):
    productos= Producto.objects.all()

    return render(request,"shop/shop.html",{"productos":productos})


