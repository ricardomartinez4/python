# -*- coding: utf-8 -*-
'''
Tratamos de centralizar en los getters y los setters el "interface interno".
y en los métodos el interface externo
'''
class Rectangulo():
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
    def perimetro(self):
        return 2 * self.base +  2 * self.altura
    
    """
    Verificación de un rectángulo:
    """
    @staticmethod
    def esValido(base, altura):
        assert(float(base) >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        assert(float(altura) >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        return True

        


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

try: 
    if Rectangulo.esValido(3, 3):
        print('El rectángulo suministrado es válido')

        
    if Cuadrado.esValido(3, 3):
        print('El cuadrado suministrado es válido')

except Exception as e:
    print('Error: ' + str(e))