class For:
    def __init__(self):
        pass

    def uso_del_For(self):
        lista_de_Nota = [(30,40),[20,40,30],(50,40,20,10)]
        acum = 0
        longi = 0
        for notas in lista_de_Nota:
            acuparcial = 0
            print(notas,end=" ")
            for nota in notas:
                print(nota)
                longi = longi+1
                acum = acum + nota
                acuparcial += nota
                promParcial = acuparcial/len(notas)
            print("Nota parcial= {} Promdio Parcial= {}".format(acuparcial,promParcial))
        prom = acum/longi
        print("Total de las Notas= {} - #Notas= {}: promedio= {} ".format(acum,longi,prom))


Obj1= For()
Obj1.uso_del_For()
