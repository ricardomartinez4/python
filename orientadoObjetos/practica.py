# -*- coding: utf-8 -*-
from builtins import staticmethod
class Palabras():
    
    __numeroFrases = 0
    
    def __init__(self,frase):
        self.frase = frase
        Palabras.__numeroFrases += 1
    @property
    def frase(self):
        return self.__frase
    @frase.setter
    def frase(self,frase):
        import re
        match = re.search('[a-zA-Z]+',frase)
        assert match, "Palabra invalida"
        self.__frase = frase 
    @property   
    def contarLetras(self):
        return len(self.frase.replace(" ",""))
    def subCadena(self,sub):
        return self.frase.count(sub)
    @classmethod
    def cuantasCreadas(cls):
        return "Numero de frases creadas: {}".format(cls.__numeroFrases)
    def __add__ (self, other):
        return Palabras(self.frase + " " + other.frase)
    def __str__(self):
        return "Su frase es: " + str(self.frase)
    def __eq__(self,other):
        if(self.frase==other.frase):
            return True
        else:
            return False
    def letrasComun(self,nuevaFrase):
        solucion = []
        for x in self.frase:
            if(x in nuevaFrase):
                solucion.append(x)
        return solucion
    @staticmethod
    def valida(frase):
        import re
        return bool(re.match("^[\sA-Za-z]*$",frase))
    def __del__(self):
        Palabras.__numeroFrases -= 1
try:
    palabra = Palabras("Hola mundo")
    print(palabra)
    palabra1 = Palabras("Hola mundo")
    palabra2 = Palabras("Adios chico")
    print(palabra.contarLetras)
    print(palabra.subCadena("mundo"))
    print(palabra.cuantasCreadas())
    print(palabra + palabra2)
    print(palabra == palabra2)
    print(palabra == palabra1)
    print(palabra.letrasComun("Hola mediterraneo"))
    del palabra2
    print(palabra.cuantasCreadas())
    print(Palabras.valida("perro"))
except Exception as e:
    print(e)
