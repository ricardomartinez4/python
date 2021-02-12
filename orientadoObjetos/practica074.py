# -*- coding: utf-8 -*-
'''
 deleters
'''
class Rectangulo():
    #
    def __init__(self, base, altura, color = 'white'):
        self.base = float(base)
        self.altura = float(altura)
        self.color = color
    def __str__(self):
        if hasattr(self, 'color'):
            return 'Rectángulo Dimensiones: ' + str(self.base) + ', ' + str(self.altura) + " de color " + self.color
        else: 
            return 'Rectángulo Dimensiones: ' + str(self.base) + ', ' + str(self.altura)
    
    # getters
    @property
    def base(self):
        return self.__base
    @property
    def altura(self):
        return self.__altura
    @property
    def color(self):
        return self.__color
    # setters
    @base.setter
    def base(self, base):
        assert(base >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        self.__base = base
    @altura.setter
    def altura(self, altura):
        assert(altura >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        self.__altura = altura
    @color.setter 
    def color(self, color):
        # Aquí deberíamos verificar los colores posibles para nuestros rectángulos
        self.__color = color
       
    #deleters   
    @color.deleter 
    def color(self):
        del self.__color
            
    # métodos
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * self.base +  2 * self.altura
    
    # métodos de clase
    @staticmethod
    def esValido(base, altura):
        assert(float(base) >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        assert(float(altura) >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        return True

try: 
    #
    # No le doy el color porque lo está tomando por defecto
    #
    rect1 = Rectangulo(3,2)
    #
    print(rect1)
    #
    del rect1.color
    #
    #del rect1.altura
    #
    print(rect1)

    
    
    # Podemos borrar
    

except Exception as e:
    print('Error: ' + str(e))