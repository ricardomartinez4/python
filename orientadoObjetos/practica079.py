# -*- coding: utf-8 -*-
'''
DNI
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
    
    # Dos métodos de clase uno privado y el otro no:
    # El no privado llama al privado
    # Realmente no nos hace falta que sea privado si queremos que se pueda ejecutar desde fuera
    @classmethod
    def __calcular_letra(cls, numero):
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return letras[int(numero)%23]
    
    @classmethod
    def devuelveLetra(cls, numero):
        return cls.__calcular_letra(numero)
    
    # setter
    @numero.setter
    def numero(self,numero):
        self.__numero = numero[0:len(numero)-1]
        assert(len(self.__numero)==8 and self.__numero.isdigit()), "DNI " + numero + " incorrecto (Número no válido)"
        # Aquí llamamos a calcular la letra:
        self.__letra = Dni.__calcular_letra(self.__numero)
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
    dni = Dni('00000000S')
    #
except Exception as e:
    print('Error: ' + str(e))