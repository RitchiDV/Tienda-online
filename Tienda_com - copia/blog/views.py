from django.shortcuts import render
from blog.models import Categoria,Post


# Create your views here.
# def services(request):


    # servicio = Servicio.objects.all()

    # return render(request,"blog/blog.html",{"servicio":servicio})


def blog(request):
    post=Post.objects.all()

     
    return render(request,"blog/blog.html",{"post":post})


def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    post=Post.objects.filter(categorias=categoria)

    return render(request,"blog/categoria.html",{"categoria":categoria,"post":post})