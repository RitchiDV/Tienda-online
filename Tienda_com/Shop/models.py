from django.db import models

# Create your models here.
class CategoriaP(models.Model):
    name= models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name="categoriap"
        verbose_name_plural="categoriasp"


    def __str__(self):
        return self.name





class Producto(models.Model):
    name=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaP, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="shop", null=True,blank=True)
    precio=models.FloatField() 
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"

    # def __str__(self):
    #     return self.name

