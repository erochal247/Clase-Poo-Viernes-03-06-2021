class For:
    def __init__(self):
        pass

    def uso_del_For(self):
        informacion=["Patricio",45,True]
        numeros=(2,5,6,4,1)
        docente = {'nombre': 'Patricio', 'edad': 45, 'faci': 'faci'}
        lista_de_Nota = [(30,40),[20,40,30],(50,40,20,10)]
        lista_de_Alumnos = [{"nombre":"Ronny","final":40},{"nombre":"Lisset","final":60},{"nombre":"Jose","final":50}]
        for i in range(5):
            print("i={}".format(i))
        for i in range(2,10):
            print("i={}".format(i))
        for i in range(4,10,2):
            print("i={}".format(i),end=" ")


        longitud = len(informacion)
        for i in range(longitud):
            print(informacion[i],end=' ')

        j=0
        while j < longitud:
            print("while",informacion[j])
            j=j+1

        for i in range(longitud-1,1,-1):
            print(informacion[i])

        for i,dato in enumerate(numeros):
            print("for",i,informacion)

        for dato in numeros:
            print(informacion)

        for dato in['h','e','l','l','o']:
            print(informacion)

        print("\nDiccionario de notas")
        for clave,valor in docente.items():
            print(clave,":",valor,end=" ")

Obj1= For()
Obj1.uso_del_For()
