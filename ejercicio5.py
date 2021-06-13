class ciclos:
    def _init_(self,num1=5):
        self.numero=num1

    def usowhile(self):
        car = input("Ingrese vocal: ")
        car = car.lower()
        while car not in('a','e','i','o','u'):
            car = input("Ingrese vocal: ").lower()
            print("felicidades el caracter:{} es una vocal".format(car))

ciclo1 = ciclos()
ciclo1.usowhile()