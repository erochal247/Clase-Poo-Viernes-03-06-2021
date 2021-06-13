class clase:
    instancia=0
    def _init_(self,dato = "Inicializacion"):
        self.frase = dato

    def usarVariable(self):
        edad, _peso = 50, 70.5
        nombres = 'Daniel Vera'
        Tipo_Sexo =  'M'
        civil = True
        ususario=()
        ususario = ('dchiki', 1234, 'hiki@gmail.com',True)
        materias = []
        materias = ['Programacion Web', 'PHP', 'POO']
        materias[1]="Python"
        materias.append("Go")
        docente = {}
        docente = {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        docente['carrera']="CS"
        # print("""Mi nombre es {}, tengo {}
        #       años""".format(nombres, edad)
        # print(ususario,materias,docente)
        # print(ususario,ususario[0],ususario[0:2],ususario[-1])
        # print(materias,materias[2:],materias[:3],materias[::],materias[-2:])
        print(docente,docente['nombre'])

ejer1 = clase()
ejer1.usarVariable()
