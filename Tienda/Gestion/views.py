from django.http import HttpResponse
from django.shortcuts import render
from  .models import Articulos
#________________________________________
from django.core.mail import send_mail #email
from django.conf import settings
from Gestion.forms import Formulario_Contacto
# Create your views here.




def Busca_un_producto(request):
    return render(request,"dis/articulos.html")


def buscar(request):

    
    if request.GET["Producto"]:

        
        #mensaje="Articulo buscado: %r" %request.GET["Producto"]
        producto = request.GET["Producto"]
        if len(producto)>20:
            mensaje= "texto de busqueda demaciado largo"

        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)
            #icontains nos devuelve  todo lo relacionado con el producto solicitado
            return render(request,"dis/Result.html",{"articulos":articulos, "query":producto})


    else:
        mensaje="no has introducido nada"

    return HttpResponse(mensaje)

#_______________________________________________________


# def contacto(request):

#     if request.method=="POST":

#         subject=request.POST["Asunto"]

#         message=request.POST["mensaje"]+ "  "+ request.POST["Email"]

#         email_from=settings.EMAIL_HOST_USER
        
#         envia_a= ["hakdigital98@gmail.com"]

#         send_mail(subject,message,email_from,envia_a)


#         return render(request, "dis/gracias.html")
    
#     return render(request,"dis/contacto.html")



def contacto(request):
    if request.method=="POST":
        mi_formulario=Formulario_Contacto(request.POST)



        if mi_formulario.is_valid():
            infForm=mi_formulario.cleaned_data
            send_mail(infForm["asunto"], infForm["mensaje"],
            infForm.get("email",""),["hakdigital98@gmail.com"],)

            return render(request,"dis/gracias.html")
    

    else:
        mi_formulario=Formulario_Contacto()

    return render(request,"dis/formsC.html",{"form":mi_formulario})