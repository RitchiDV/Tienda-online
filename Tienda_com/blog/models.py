from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
#user= para relacionar cada post con un usuario u autor de cada post
#esto sirve para 1 a muchos

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:  #Meta opcion
        verbose_name="categoria"
        verbose_name="categorias" 


    def __str__(self):
        return self.nombre

    
class Post(models.Model):
    titulo=models.CharField(max_length=50)
    Contenido= models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="blog", null=True, blank=True)#para manipular imagenes se tiene que instalar
    #pip install pillow
    autor=models.ForeignKey(User,on_delete=models.CASCADE)#on delete: cuando se elimine el usuario se hara una eliminacion en cascada
    #foreingkey relacion entre el usuario y el post y cuando se de de baja al igual se elimina los post del usuario
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:  #Meta opcion
        verbose_name="Post"
        verbose_name="post's" 


    def __str__(self):
        return self.titulo