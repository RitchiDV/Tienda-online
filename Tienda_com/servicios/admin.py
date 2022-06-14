from django.contrib import admin
from.models import Servicio # importamos de models.py la class Servicio

#________________________________
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    #created y updated son de tipo dato eso se actualiza automaticamente

admin.site.register(Servicio,ServicioAdmin) #registramos el models.py-Servicio al admin
