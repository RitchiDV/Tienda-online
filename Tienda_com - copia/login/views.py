from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.

class VRegistro(View):

    def get(self,request):

        form=UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})


    def post(self,request): 
        

        form=UserCreationForm(request.POST)


        if form.is_valid():

            usuario=form.save()
            
            #al mandar el post al mismo tiempo hace un login y entra en la session del usuraio

            login(request,usuario)

            return redirect("Home")
        else:
            for mssg in form.error_messages:
                messages.error(request, form.error_messages[mssg])

            return render(request,"registro/registro.html",{"form":form})


def log_out(request):
    logout(request)

    return redirect("Home")


def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=nombre_usuario,password=password)
            if user is not None:
                login(request,user)
                return redirect("Home")
            else:
                messages.error(request,"user is invalid")
        else:
            messages.error(request, "informacion incorrecta")
            
    form=AuthenticationForm()

    return render(request, "login/login.html",{"form":form})
    
