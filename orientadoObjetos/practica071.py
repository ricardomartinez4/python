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
        # Utilizamos los getters:
        return 'Rectángulo Dimensiones: ' + str(self.base) + ', ' + str(self.altura)
    """
    
    PASAMOS A QUE base SEA UN ATRIBUTO PROTEGIDO EN VEZ DE PRIVADO
    
    público: 
    protegido: _
    privado: __
    
    """
    @property
    def base(self):
        return self._base
    @property
    def altura(self):
        return self.__altura
    #
    @base.setter
    def base(self, base):
        assert(base >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        self._base = base
    @altura.setter
    def altura(self, altura):
        assert(altura >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        self.__altura = altura
            
    # Utilizamos los getters
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * self.base +  2 * self.altura


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        #super().__init__(lado, lado)
        Rectangulo.__init__(self, lado, lado)
    def __str__(self):
        # NOS FIJAMOS EN LOS POSIBLES ACCESO A LOS DATOS
        #return 'Cuadrado de lado ' + str(self.base)
        # Accedemos a él como protegido
        return 'Cuadrado de lado ' + str(self._base)
        """
        ver las opciones de los protegidos
        """
    @property
    def lado(self):
        return self.base
    @lado.setter
    def lado(self, nuevoLado):
        self.base = nuevoLado
        self.altura = nuevoLado

try: 
    rectangulo = Rectangulo(3,2)
    
    cuadrado = Cuadrado(3)
    print(cuadrado)
    print(cuadrado.perimetro())
    print(cuadrado.area())
    
    cuadrado.lado = 4
    print(cuadrado)
    print(cuadrado.perimetro())
    print(cuadrado.area())
    

except Exception as e:
    print('Error: ' + str(e))