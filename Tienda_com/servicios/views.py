from django.shortcuts import render
from servicios.models import Servicio

def services(request):


    servicio = Servicio.objects.all()

    return render(request,"servicios/services.html",{"servicio":servicio})