"""
articulo
cliente 
venta 
venta det
"""
class Articulo:
    def __init__(self,cod,des,pre,stoc):
        self.codigo=cod
        self.descripcion=des
        self.precio=pre
        self.stock=stoc

class Cliente:
    def __init__(self,ced,nom,dir,tel):
        self.cedula=ced
        self.nombre=nom
        self.direccion=dir
        self.telefono=tel

class Venta:
    def __init__(self,fac,fec,cliente,tot,detalle):
        self.factura=fac
        self.fecha=fec
        self.cliente=cliente
        self.total=tot
        self.detalle=detalle

class ventaDet:
    def __init__(self,venta,articulo,precio,cantida):
        self.articulo=articulo
        self.precio=precio
        self.cantida=cantida
