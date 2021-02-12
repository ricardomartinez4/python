# -*- coding: utf-8 -*-
"""
Hacer una clase triangulo herendando 
"""
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def perimetro(self):
        """
        No es obligatorio especificar el tipo que será devuelto pero sí es bueno para ayudar en la programación
        ES INFORMATIVO.
        """
        pass
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def queSoy(self):
        return "Soy una figura"

class Rectangulo(Shape):
    # Aqui tendremos almacenados el numero de rectangulos que hemos creado
    __numRectangulos = 0
    # Constructor
    def __init__(self, base, altura):
        self.base = base 
        self.altura = altura
        Rectangulo.__numRectangulos += 1
    # Print mediante str
    def __str__(self):
        return "Rectángulo de altura " + str(self.altura) + " y base " + str(self.base)
    # getters 
    @property
    def base(self):
        return self.__base
    @property
    def altura(self):
        return self.__altura
    # setters
    @altura.setter
    def altura(self, nuevaAltura):
        assert(float(nuevaAltura) > 0), 'El lado suministrado no es válido'
        self.__altura = float(nuevaAltura)
    @base.setter
    def base(self, nuevaBase):
        assert(float(nuevaBase) > 0), 'El lado suministrado no es v�lido'
        self.__base = float(nuevaBase)

    #
    # Al ser Shape de la clase ABC tenemos que crear los m�todos pe�metro y �rea
    #
    def perimetro(self):
        return 2 * self.altura + 2 * self.base
    def area(self):
        return self.altura + self.base
    def queSoy(self):
        return "Soy un rect�ngulo"
    @classmethod
    def numRectangulos(cls):
        return cls.__numRectangulos

class Triangulo(Shape):
    __numTriangulos = 0
    def __init__(self, lado1, lado2, lado3, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.altura = altura
        Triangulo.__numTriangulos += 1
        
    def __str__(self):
        return "Triangulo con lados: " + str(self.lado1) + ", " + str(self.lado2) + " y " + str(self.lado3) + ". Con una altura de " + str(self.__altura)
    def area(self):
        return self.lado1 * self.altura / 2 
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    def queSoy(self):
        return "Soy un triangulo"
    @property
    def lado1(self):
        return self.__lado1
    @property
    def lado2(self):
        return self.__lado2
    @property
    def lado3(self):
        return self.__lado3
    @property
    def altura(self):
        return self.__altura
    @lado1.setter
    def lado1(self, nuevoLado1):
        assert(float(nuevoLado1) > 0), 'El lado suministrado no es válido'
        self.__lado1 = float(nuevoLado1)
    @lado2.setter
    def lado2(self, nuevoLado2):
        assert(float(nuevoLado2) > 0), 'El lado suministrado no es válido'
        self.__lado2 = float(nuevoLado2)
    @lado3.setter
    def lado3(self, nuevoLado3):
        assert(float(nuevoLado3) > 0), 'El lado suministrado no es válido'
        self.__lado3 = float(nuevoLado3)
    @altura.setter
    def altura(self, nuevaAltura):
        assert(float(nuevaAltura) > 0), 'La altura suministrada no es válida'
        self.__altura = float(nuevaAltura)
    @classmethod
    def numTriangulos(cls):
        return cls.__numTriangulos
class Isosceles(Triangulo):
    def __init__(self,lado1,lado2,altura):
        Triangulo.__init__(self, lado1, lado2, lado2, altura)
    def __str__(self):
        return "Triangulo isosceles con lados: " + str(self.lado1) + " y " + str(self.lado2) + ". Con una altura de " + str(self.altura)
    def queSoy(self):
        return "Soy un triangulo isosceles"
    @Triangulo.lado2.setter
    def lado2(self,lado):
        Triangulo.lado2.fset(self,lado)
        Triangulo.lado3.fset(self,lado)
    @Triangulo.lado3.setter
    def lado3(self,lado):
        Triangulo.lado2.fset(self,lado)
        Triangulo.lado3.fset(self,lado)

class Equilatero(Isosceles):
    def __init__(self,lado1,altura):
        Isosceles.__init__(self, lado1, lado1, altura)
    def __str__(self):
        return "Triangulo equilatero con lados de: " + str(self.lado1) + " y " + "con una altura de " + str(self.altura)
    def queSoy(self):
        return "Soy un triangulo equilatero"
    @Isosceles.lado2.setter
    def lado2(self,lado):
        Isosceles.lado1.fset(self,lado)
        Isosceles.lado2.fset(self,lado)
try:
    tri = Triangulo(2,8,3,7)
    print(tri)
    print(tri.perimetro())
    print(tri.area())
    print("-"*80)
    
    isosceles1 = Isosceles(5,8,10)
    print(isosceles1)
    print(isosceles1.area())
    print(isosceles1.perimetro())
    print("-"*80)
    
    equilatero1 = Equilatero(5,14)
    print(equilatero1)
    print(equilatero1.area())
    print(equilatero1.perimetro())
    print('-'*80)
    
    rectangulo1 = Rectangulo(5,8)
    rectangulo2 = Rectangulo(8,9)
    print('Número de rectangulos creados: ' + str(rectangulo1.numRectangulos()))
    

except Exception as e:
    print(e)