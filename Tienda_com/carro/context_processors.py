def importe_total_carro(request):
    Total=0

    
    if "carro" in request.session:
        if request.user.is_authenticated:
            for key,value in request.session["carro"].items():
                    Total=Total+float(value["precio"])

        else:
            Total="debes logearte primero"

        return {"importe_total_carro":Total}
    


    return {"importe_total_carro":Total}








#     # Regresa Total=0 si el key 'carro' no existe en la sesión
#     # Aqui manejarlo como mejor te convenga
#     return Total