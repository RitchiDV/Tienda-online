from django.db import models

class Clientes(models.Model):
    nombre =models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name="la direccion")#modifica en el admin  el nombre direccion
    email=models.EmailField(blank=True,null=True)#blank=True,null=True: hace que el espacio sea opcional y no obligatoria
    tfno=models.CharField(max_length=7)
    # def __str__(self):
    #     return"name: %s  direccion: %s email: %s telefono: %s"%(self.nombre,self.direccion,self.email,self.tfno)



class Articulos(models.Model):
    nombre= models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    
    def __str__(self):
        return "el nombre es %s la seccion es %s y el precio es %s" % (self.nombre,self.seccion,self.precio)




class pedidos (models.Model):
    numero= models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()