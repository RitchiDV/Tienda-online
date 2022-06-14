from django.db import models

from django.contrib.auth import get_user_model

from Shop.models import Producto

from django.db.models import F,Sum,FloatField
# Create your models here.

User=get_user_model()



class Pedido(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id


    @property
    def total(self):
        return self.lineapedido_set_aggregate(
            total=Sum(F("precio")*F("cantidad"),output_field=FloatField())
        )["total"]


    class Meta:
        db_table="pedidos"
        verbose_name="pedido"
        verbose_name="pedidos"
        ordering=["id"]

class Linea_pedido(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    producto_id=models.ForeignKey(Producto,on_delete=models.CASCADE)
    pedido_id=models.ForeignKey(Pedido,on_delete=models.CASCADE)
    created_ad=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.cantidad} unidades de {self.producto_id.name}"


    class Meta:
        db_table="lineapedido"
        verbose_name="linea pedido"
        verbose_name="linea pedidos"
        ordering=["id"]

