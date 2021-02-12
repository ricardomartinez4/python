# -*- coding: utf-8 -*-
'''
DNI
A staticmethod is a method that knows nothing about the class or instance it was called on. 
It just gets the arguments that were passed, no implicit first argument. 

A classmethod, on the other hand, is a method that gets passed the class it was called on, 
or the class of the instance it was called on, as first argument. 
This is useful when you want the method to be a factory for the class: 
since it gets the actual class it was called on as first argument, 
you can always instantiate the right class, even when subclasses are involved. 

inspect

'''

import inspect

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
        print("Vemos que es la clase :" + str(cls))
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

try:
    dni = Dni('00000000T')
    print(dni)
    print(dni.numero)
    print(dni.letra)
    print(Dni.devuelveLetra('24342989'))
    #
    # Da error: print(Dni.__calcular_letra('24342989'))
    #
    #dni = Dni('00000000S')
    #
    print('-------------métodos de la clase-------------------')
    for name, data in inspect.getmembers(Dni, inspect.ismethod):
        print('{} : {!r}'.format(name, data))
    print('-------------funciones de la clase-------------------')
    for name, data in inspect.getmembers(Dni, inspect.isfunction):
        print('{} : {!r}'.format(name, data))
except Exception as e:
    print('Error: ' + str(e))