# -*- coding: utf-8 -*-
'''
Objetos de la misma clase son distintos
'''
class Dog():
    pass 

try:
    # Creamos dos instancias de la clase
    perro1 = Dog()
    perro2 = Dog()
    # Vemos la posición en memoria de cada una de ellas
    print(perro1)
    print(perro2)
    # Vemos si ambas son iguales
    print(perro1 == perro2)
    #
except Exception as e:
    print("Error " + str(e))