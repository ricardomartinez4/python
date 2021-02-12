# -*- coding: utf-8 -*-
'''
Clases dentro de clases

'''

class Dni():

    def __init__(self, numero):
        self.numero=numero

    def __str__(self):
        return "{0}-{1}".format(self.numero,self.letra)
    
    # getters
    @property
    def numero(self):
        return self.__numero
    
    @property
    def letra(self):
        return self.__letra
    
    @classmethod
    def devuelveLetra(cls, numero):
        # cls: Hace referencia a la clase, es un método de clase
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return letras[int(numero)%23]

    # setter
    @numero.setter
    def numero(self,numero):
        self.__numero = numero[0:len(numero)-1]
        assert(len(self.__numero)==8 and self.__numero.isdigit()), "DNI " + numero + " incorrecto (Número no válido)"
        # Aquí llamamos a calcular la letra, llamamos al método de clase:
        self.__letra = Dni.devuelveLetra(self.__numero)
        #
        assert(self.__letra == numero[-1]),  "DNI " + numero + " incorrecto (letra no válida)"

class Person():
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.__dni = dni
        #
        # Falta verificar que el dni es instancia de la clase Dni
        #
        #
    def __str__(self):
        return "Nombre: " + self.nombre + " con dni " + str(self.dni)
    
    # getters
    @property
    def dni(self):
        return self.__dni
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

try:
    dni = Dni('00000000T')
    person = Person('Antonio', dni)
    print(person)
    #------------------------------------------
    print("The globals() method returns the dictionary of the current global symbol table.")
    print( list(globals().keys()))
    #
    print(list(filter(lambda x: x.find("__") == -1, list(globals().keys()))))
    # Al borrar la persona sigue existiendo el dni
    del person
    print(dni)
    print(list(filter(lambda x: x.find("__") == -1, list(globals().keys()))))
    #
except Exception as e:
    print('Error: ' + str(e))