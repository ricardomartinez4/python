# -*- coding: utf-8 -*-
'''
'''
class Rectangulo():
    #
    def __init__(self, base, altura):
        
        
        #
        # La verificación de las restricciones no se están haciendo
        #
        
        self.__base = float(base)       # Se denomina variable de instancia
        self.__altura = float(altura)
    def __str__(self):
        return 'Rectángulo Dimensiones: ' + str(self.__base) + ', ' + str(self.__altura)
    
    # getters 
    @property
    def base(self):
        return self.__base
    @property
    def altura(self):
        return self.__altura
    
    # setters (Los setters no devuelven ningún valor, en principio)
    @base.setter
    def base(self, base):
        if (base < 0):
            raise ValueError('La base no puede ser negativa')
        else: 
            self.__base = base
    @altura.setter
    def altura(self, altura):
        if (altura < 0):
            raise ValueError('La altura no puede ser negativa')
        else: 
            self.__altura = altura
            
    # métodos
    def area(self):
        return self.__base * self.__altura
    def perimetro(self):
        return 2 * self.__base +  2 * self.__altura


try: 
    rectangulo = Rectangulo(-3,2)
    
    print(rectangulo)
    print(rectangulo.altura)
    print(rectangulo.base)
    rectangulo.altura = 4
    print("Nueva altura: " + str(rectangulo.altura))
    print(rectangulo.area())
    print(rectangulo.perimetro())
    
except Exception as e:
    print('Error: ' + str(e))