# -*- coding: utf-8 -*-
'''
Variables de clase/ Atributo de clase
destructores
métodos de clase

'''
class Rectangulo():
    # Variables de clase
    shape = "Rectángulo"         # pública
    __tipo = "Figura"            # privado
    _otroTipo = "Otra Figura"    # protegida
    
    
    __numRectangulos = 0 # privada
    
    #
    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)
        Rectangulo.__numRectangulos += 1
        
    def __str__(self):
        return 'Rectángulo Dimensiones: ' + str(self.base) + ', ' + str(self.altura)
    # Es un destructor:
    def __del__(self):
        # Cuando borramos la instancia queremos que quede reflejado en el número de rectñangulos que tenemos
        Rectangulo.__numRectangulos -= 1
    
    # getters
    @property
    def base(self):
        return self.__base
    @property
    def altura(self):
        return self.__altura
    # setters
    @base.setter
    def base(self, base):
        assert(base >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        self.__base = base
    @altura.setter
    def altura(self, altura):
        assert(altura >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        self.__altura = altura
            
    # métodos
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * self.base +  2 * self.altura
    
    # métodos estático
    @staticmethod
    def esValido(base, altura):
        assert(float(base) > 0), 'Ninguno de los lados de la figura pueden ser negativos'
        assert(float(altura) > 0), 'Ninguno de los lados de la figura pueden ser negativos'
        return True
    
    # método de clase
    @classmethod
    def queTipoSoy(cls):
        return cls.__tipo
    
    @classmethod
    def numRectangulos(cls):
        return cls.__numRectangulos
    
    
    
    # Sobrecarga de operadores
    def __add__ (self, other):
        return Rectangulo(self.base + other.base, self.altura + other.altura)
    def __eq__(self, other):
        # Suponemos que son iguales si sus perímetros son el mismo
        return self.perimetro() == other.perimetro()

try: 
    rect1 = Rectangulo(3,2)
    rect2 = Rectangulo(3,2)
    #
    print("Número actual de rectángulos: " + str(Rectangulo.numRectangulos()))
    #
    if (rect1 == rect2):
        rect3 = rect1 + rect2
        print(rect3)
        # Ahora borramos el objeto rect3
        del rect3
    else: 
        print('Los rectángulos no tienen el mismo perímetro')
    
    # Otra prueba
    rect1 += rect2
    print(rect1)
    
    #
    print("rect1 es un " + rect1.shape)
    print("rect2 es un " + rect2.shape)
    print("Todos los elementos de Rectangulo son  " + Rectangulo.shape + "s")
    #
    print("Número actual de rectángulos (rect1): " + str(rect1.numRectangulos()))
    print("Número actual de rectángulos: (Rectangulo): " + str(Rectangulo.numRectangulos()))
    #
    # Error: print(Rectangulo.__tipo) porque es privada aunque sea de clase
    print("Yo soy una: "+ Rectangulo.queTipoSoy())
    
    print(str(Rectangulo.queTipoSoy)  + "\nNote: the bound method is recreated *every time* you call it \n se denomina método enlazado porque, cuando se invoca, sabe que debe proporcionar el objeto al que estaba vinculado como primer argumento")
    
    print(Rectangulo.esValido)
    print(Rectangulo.esValido(3, 1))
    print(Rectangulo.esValido(-3, 1))
    

except Exception as e:
    print('Error: ' + str(e))
    
  