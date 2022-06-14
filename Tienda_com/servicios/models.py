from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    Contenido= models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="servicios")#para manipular imagenes se tiene que instalar
    #pip install pillow
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:  #Meta opcion
        verbose_name="servicio"
        verbose_name="servicios" 


    def __str__(self):
        return self.titulo