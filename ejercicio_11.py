from ejercicio10 import Cargo

class Empleado:
    secuencia=0
    def __init__(self,nom,ced,sue,ejercici10):
        self.codigo=self.generarCodigo
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=ejercici10
    def mostrar(self):
        print("codigo:{} nombre:{} cargo:{}-{}".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.description))

    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia

cargo1= Cargo("Docente")
emp1= Empleado("Ivan","0922562345",700,cargo1)
emp1.mostrar()
cargo2= Cargo("Analista")
emp2= Empleado("Eduardo","0929562345",800,cargo2)
emp2.mostrar()
 
