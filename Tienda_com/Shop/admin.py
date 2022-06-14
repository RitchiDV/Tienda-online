from django.contrib import admin
from Shop.models import CategoriaP,Producto
# Register your models here.

class CategoriaPAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated",)
    search_fields=("name",)
    list_filter=("name",)

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated",)
    list_display=("name","categorias","precio","disponibilidad")
    search_fields=("name","categorias",)
    list_filter=("categorias",)


admin.site.register(CategoriaP,CategoriaPAdmin)
admin.site.register(Producto,ProductoAdmin)