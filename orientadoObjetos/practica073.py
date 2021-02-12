# -*- coding: utf-8 -*-
'''
Tratamos de centralizar en los getters y los setters el "interface interno".
y en los métodos el interface externo
'''
class Rectangulo():
    
    
    """
    The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
    """
    
    #
    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)
    def __str__(self):
        return 'Rectángulo Dimensiones: ' + str(self.base) + ', ' + str(self.altura)

    @property
    def base(self):
        return self.__base
    @property
    def altura(self):
        return self.__altura
    #
    @base.setter
    def base(self, base):
        assert(base >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        self.__base = base
    @altura.setter
    def altura(self, altura):
        assert(altura >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        self.__altura = altura
            
    # Utilizamos los getters
    def area(self):
        return self.base * self.altura
    
    """
    Podemos hacer lo siguiente para ejecutar un método de clase, pero no tiene mucho sentido el hacerlo
    """
    def perimetro(self):
        return Rectangulo.perimetroRectangulo(self.base, self.altura)
    
    """
    Verificación de un rectángulo:
    """
    @staticmethod
    def esValido(base, altura):
        assert(float(base) >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        assert(float(altura) >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        return True
        
    """
    Creamos el método de clase para obtener el perímetro de un rectángulo
    """
    @staticmethod
    def perimetroRectangulo(base, altura):
        return 2 * base +  2 * altura


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        #super().__init__(lado, lado)
        Rectangulo.__init__(self, lado, lado)
    def __str__(self):
        return 'Cuadrado de lado ' + str(self.base)
    @property
    def lado(self):
        return self.base
    @lado.setter
    def lado(self, nuevoLado):
        self.base = nuevoLado
        self.altura = nuevoLado
        
    @staticmethod
    def esValido(lado):
        return Rectangulo.esValido(lado, lado)
    

try: 
    if Rectangulo.esValido(3, 3):
        print(Rectangulo.perimetroRectangulo(3,3))
        
    if Cuadrado.esValido(3):
        print("Cuadrado válido")
        
        
    rectangulo = Rectangulo(3,2)
    
    print(rectangulo)
    print(rectangulo.perimetro())
    
    print(Rectangulo(3,3).perimetro())

except Exception as e:
    print('Error: ' + str(e))