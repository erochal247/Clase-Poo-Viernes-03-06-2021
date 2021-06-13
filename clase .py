# num=20
# if type(num)== int:
#     print("La respuesta: ",num*2)
# else:
#     print("El dato no es numerico")

# def mensaje(men):
#     print(men)

# mensaje("Mi primer programa")
# mensaje("Mi segundo programa")

# class clase:
#     def variables(self):
#         edad,_peso = 50,70.50
#         print(edad,_peso)


# ej1 = clase()
# ej1.variables()


# class clase:
#     instancia=0
#     def _init_(self,dato = "Inicializacion"):
#         self.frase = dato

#     def usarVariable(self):
#         edad, _peso = 50, 70.5
#         nombres = 'Daniel Vera'
#         Tipo_Sexo =  'M'
#         civil = True
#         ususario=()
#         ususario = ('dchiki', 1234, 'hiki@gmail.com',True)
#         materias = []
#         materias = ['Programacion Web', 'PHP', 'POO']
#         materias[1]="Python"
#         materias.append("Go")
#         docente = {}
#         docente = {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
#         docente['carrera']="CS"
#         # print("""Mi nombre es {}, tengo {}
#         #       años""".format(nombres, edad)
#         # print(ususario,materias,docente)
#         # print(ususario,ususario[0],ususario[0:2],ususario[-1])
#         # print(materias,materias[2:],materias[:3],materias[::],materias[-2:])
#         print(docente,docente['nombre'])

# ejer1 = clase()
# ejer1.usarVariable()

# CONDICIONES
# class condicion:
#     contador=0
#     def _init_(self,num1=0,num2=1):
#         self.numero1=num1
#         self.numero2=num2
#         # numero = num1+num2
#         self.numero3 = num1

#     def usoIf(self):
#         if self.numero1 == self.numero2:
#             print("numero1:{}, numero2:{}: son iguales".format(self.numero1, self.numero2))
#         elif self.numero1 == self.numero3:
#             print("numero1:{}, numero3:{}: son iguales".format(self.numero1, self.numero3))
#         else:
#             print("no son iguales ")
# # cond1 = condicion()
# # print=(cond1.numero1)
# # print=(cond1.numero2)

# cond2 =condicion(10,20)
# cond2.usoIf()
# print(cond2.numero1)

# CICLOS
class ciclos:
    def _init_(self,num1=5):
        self.numero=num1

    def usowhile(self):
         car = input("Ingrese vocal")
         car = car.lower()
         while car in('a','e','i','o','u'):
            car = input("Ingrese vocal: ").lower()
         print("felicidades el caracter:{} es una vocal".format(car))

ciclo1 = ciclos()
ciclo1.usowhile()