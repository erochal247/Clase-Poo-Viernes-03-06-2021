class For:
    def __init__(self):
        pass

    def uso_del_For(self):
        lista_de_Alumnos = [{"nombre":"Ronny","final":40},{"nombre":"Lisset","final":60},{"nombre":"Jose","final":50}]
        acum=0
        cont=0
        for alumnos in lista_de_Alumnos:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave,":",valor,end=" ")
                if clave=="final": acum=acum+valor
            cont+=1
        print(acum/cont)

Obj1= For()
Obj1.uso_del_For()

