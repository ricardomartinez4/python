# -*- coding: utf-8 -*-
'''
'''
class Rectangulo():
    #
    def __init__(self, base, altura, color='white'):
        # Ahora en vez de iniciar los atributos se utilizan los métodos getter
        self.base = float(base)
        self.altura = float(altura)
        self.color = color
    def __str__(self):
        return 'Rectángulo Dimensiones: ' + str(self.__base) + ', ' + str(self.__altura)
    #
    @property
    def base(self):
        return self.__base
    @property
    def altura(self):
        return self.__altura
    #
    @base.setter
    def base(self, base):
        assert(base >= 0), 'La base no puede ser negativa'
        self.__base = float(base)
    @altura.setter
    def altura(self, altura):
        assert(altura >= 0), 'La altura no puede ser negativa'
        self.__altura = float(altura)
            
    def area(self):
        return self.__base * self.__altura
    def perimetro(self):
        return 2 * self.__base +  2 * self.__altura


try: 
    #rectangulo = Rectangulo(-3,2)
    rectangulo = Rectangulo(3,2)
    
    print(rectangulo)
    print(rectangulo.altura)
    print(rectangulo.color)
    rectangulo.color = 'black'
    print(rectangulo.color)
    rectangulo.altura = 4
    print(rectangulo)
    
    print(rectangulo.area())
    print(rectangulo.perimetro())
    

except Exception as e:
    print('Error: ' + str(e))# -*- coding: utf-8 -*-
'''
'''
class Rectangulo():
    #
    def __init__(self, base, altura, color='white'):
        # Ahora en vez de iniciar los atributos se utilizan los métodos getter
        self.base = float(base)
        self.altura = float(altura)
        self.color = color
    def __str__(self):
        return 'Rectángulo Dimensiones: ' + str(self.__base) + ', ' + str(self.__altura)
    #
    @property
    def base(self):
        return self.__base
    @property
    def altura(self):
        return self.__altura
    #
    @base.setter
    def base(self, base):
        assert(base >= 0), 'La base no puede ser negativa'
        self.__base = float(base)
    @altura.setter
    def altura(self, altura):
        assert(altura >= 0), 'La altura no puede ser negativa'
        self.__altura = float(altura)
            
    def area(self):
        return self.__base * self.__altura
    def perimetro(self):
        return 2 * self.__base +  2 * self.__altura


try: 
    #rectangulo = Rectangulo(-3,2)
    rectangulo = Rectangulo(3,2)
    
    print(rectangulo)
    print(rectangulo.altura)
    print(rectangulo.color)
    rectangulo.color = 'black'
    print(rectangulo.color)
    rectangulo.altura = 4
    print(rectangulo)
    
    print(rectangulo.area())
    print(rectangulo.perimetro())
    

except Exception as e:
    print('Error: ' + str(e))