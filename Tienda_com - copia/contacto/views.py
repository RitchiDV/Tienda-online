
# Create your views here
from django.shortcuts import redirect, render
from .forms import Forms_Contacto
from django.core.mail import EmailMessage

def contacto(request):

    formulario_contacto=Forms_Contacto()

    if request.method== "POST":
        formulario_contacto=Forms_Contacto(data=request.POST)
        if formulario_contacto.is_valid():
            name=request.POST.get("name")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("mensaje desde app Django",
            "El usuario con nombre {} con la direccion {} escribe lo siquiente:\n\n {}".format(name,email,contenido),
            "",["hakdigital98@gmail.com"],reply_to=[email]
            )
            try:
                email.send()

                return redirect("/Contacto/?OK")
            except:
                return redirect("/Contacto/?Novalido")

    return render(request,"contacto/contacto.html",{"miformulario":formulario_contacto})