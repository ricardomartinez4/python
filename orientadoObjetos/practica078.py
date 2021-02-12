# -*- coding: utf-8 -*-
'''
DNI

uso de inspect

método privado

'''

import inspect

class Dni():

    def __init__(self, numero):
        # Ejemplo: numero= '24342989L'
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
    
    # método privado:
    def __calcular_letra(self):
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return letras[int(self.numero)%23]
    
    @staticmethod
    def devuelveLetra(numero):
        print('Calcula letra de ' + str(numero))
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return letras[int(numero)%23]

    # setter
    @numero.setter
    def numero(self,numero):
        self.__numero = numero[0:len(numero)-1]
        assert(len(self.__numero)==8 and self.__numero.isdigit()), "DNI " + numero + " incorrecto (Número no válido)"
        self.__letra = self.__calcular_letra()
        assert(self.__letra == numero[-1]),  "DNI " + numero + " incorrecto (letra no válida)"

try:
    dni = Dni('00000000T')
    print(dni)
    print(dni.numero)
    print(dni.letra)
    print(Dni.devuelveLetra('24342989'))
    #
    # Lo siguiente da error porque es privado: print(dni.__calcular_letra())
    #
    #dni = Dni('00000000S')
    #
    # Ahora obtenemos unos cuantos más datos:
    print("Es función devuelveLetra? " + str(inspect.isfunction(Dni.devuelveLetra)))
    print("Es método devuelveLetra? " + str(inspect.ismethod(Dni.devuelveLetra)))
    print("Es función letra? " + str(inspect.isfunction(Dni.letra)))
    print("Es método letra? " + str(inspect.ismethod(Dni.letra)))
    print("Es clase Dni? " + str(inspect.isclass(Dni)))
    print("Es clase dni? " + str(inspect.isclass(dni)))
    """
    My rule of thumb: __repr__ is for developers, __str__ is for customers.
    This is true because for 
        obj = uuid.uuid1(), obj.__str__() is "2d7fc7f0-7706-11e9-94ae-0242ac110002" and 
        obj.__repr__() is "UUID('2d7fc7f0-7706-11e9-94ae-0242ac110002')". 
        Developers need (value + origin) whereas customers need a value and they don't care how they got it!
     
    !r - convert the value to a string using repr().
        
    !s - convert the value to a string using str().
        The goal of __str__ is to be readable
        Specifically, it is not intended to be unambiguous — notice that str(3)==str("3")
    """
    print('-------------métodos de la clase-------------------')
    for name, data in inspect.getmembers(Dni, inspect.ismethod):
        print('{} : {!r}'.format(name, data))
    print('-------------funciones de la clase-------------------')
    for name, data in inspect.getmembers(Dni, inspect.isfunction):
        print('{} : {!r}'.format(name, data))
    print('-------------Todos los miembros de la clase-------------------')
    for name, data in inspect.getmembers(Dni):
        print('{} : {!r}'.format(name, data))
    #
except Exception as e:
    print('Error: ' + str(e))