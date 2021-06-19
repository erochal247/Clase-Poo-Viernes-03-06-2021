frase = "Hola Mundo como estas"
vocales = []
if car in {'a','e','i','o','u'}:
    vocales.append(car)
print(vocales)



print([car for car in "Hola Mundo como estas" if car in ('a','e','i','o','u')])
