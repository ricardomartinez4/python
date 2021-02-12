# -*- coding: utf-8 -*-
"""
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def perimetro(self) -> float:
        """
        No es obligatorio especificar el tipo que será devuelto pero sí es bueno para ayudar en la programación
        Es informativo
        """
        pass
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def queSoy(self) -> str:
        return "Soy una figura"

class Rectangulo(Shape):
    # Constructor
    def __init__(self, base, altura):
        self.base = base 
        self.altura = altura
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
        assert(float(nuevaBase) > 0), 'El lado suministrado no es válido'
        self.__base = float(nuevaBase)

    #
    # Al ser Shape de la clase ABC tenemos que crear los métodos peímetro y área
    #
    def perimetro(self):
        return 2 * self.altura + 2 * self.base
    def area(self):
        return self.altura + self.base
    def queSoy(self):
        return "Soy un rectángulo"
    
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        Rectangulo.__init__(self, lado, lado)
    def __str__(self):
        return "Cuadrado de lado " + str(self.base)
    def queSoy(self):
        return "Soy un cuadrado"
 
if __name__ == "__main__":
    try:
        shape1 = Cuadrado(2)
        #
        #
        #
        #
        print(shape1)
        print(shape1.__str__())
        #
        #
        #
        #
        #
        print(shape1.perimetro())
        print(shape1.area())
        # Voy a ejecutar la misma función desde puntos de vista distintos
        # Porque como parámetro tienen el self
        print(shape1.queSoy())
        # Si no tuviera el queSoy en Cuadrado sabemos que subiría y ejecutaría el del Rectángulo
        print(Rectangulo.queSoy(shape1))
        print(Shape.queSoy(shape1))
        
        
        
        ##
        #
        print(issubclass(Cuadrado, Rectangulo))
        print(issubclass(Cuadrado, Shape))
        print(issubclass(Cuadrado, ABC))
        
    except Exception as e:
        print('Error: ' + str(e))