
class Carro:

    #manejo de session
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        self.carro=carro


    #agregando productos
    def agregar(self,producto):
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "name":producto.name,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url,
            }
        else:
            for key,value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio
                    break
        self.guardar_carro()



 #guardando movimientos de session de carro
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

 #elimina producto si el id del producto coincide
    def eliminar(self,producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    #resta el producto pero en caso de que sea menor que 0 se 
    #llama la funcion eliminar producto y despues un break
    def restar_producto(self,producto):
        for key,value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]=float(value["precio"])-producto.precio
                
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()#guarda los movimientos





    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True

