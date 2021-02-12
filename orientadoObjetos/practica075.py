# -*- coding: utf-8 -*-
'''
Sobrecarga de operadores
Borrar objetos
'''
class Rectangulo():
    #
    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)
    def __str__(self):
        return 'Rectángulo Dimensiones: ' + str(self.base) + ', ' + str(self.altura)
    
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
    
    # métodos de clase
    @staticmethod
    def esValido(base, altura):
        assert(float(base) >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        assert(float(altura) >= 0), 'Ninguno de los lados de la figura pueden ser negativos'
        return True
    
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
    
    # Podemos borrar
    

except Exception as e:
    print('Error: ' + str(e))
    
    
"""
Nota: el uso de other como nombre de variable no es obligatorio, pero se considera la norma.

Operador                    Método                    Expresión
+ Adición                  __add__(self, other)        a1 + a2
- Resta                    __sub__(self, other)        a1 - a2
* Multiplicación           __mul__(self, other)        a1 * a2
@ Matrix Multiplication    __matmul__(self, other)     a1 @ a2 ( Python 3.5 )
/ División                 __truediv__(self, other)    a1 / a2 ( Python 3 )
// División entera         __floordiv__(self, other)   a1 // a2
% Modulo / resto           __mod__(self, other)        a1 % a2
** Potencia                __pow__(self, other[, modulo])    a1 ** a2
<< Bitwise Left Shift      __lshift__(self, other)    a1 << a2
>> Bitwise Right Shift     __rshift__(self, other)    a1 >> a2
& Bitwise Y                __and__(self, other)       a1 & a2
^ Bitwise XOR              __xor__(self, other)       a1 ^ a2
| (Bitwise OR)             __or__(self, other)        a1 | a2
- Negación (Aritmética)    __neg__(self)              -a1
+ Positivo                 __pos__(self)              +a1
~ Bitwise NO               __invert__(self)           ~a1
< Menos que                __lt__(self, other)        a1 < a2
<= Menor que o igual a     __le__(self, other)        a1 <= a2
== Igual a                 __eq__(self, other)        a1 == a2
!= No es igual a           __ne__(self, other)        a1 != a2
> Mayor que                __gt__(self, other)        a1 > a2
>= Mayor que o igual a     __ge__(self, other)        a1 >= a2
[index] operador de índice __getitem__(self, index)   a1[index]
in En operador             __contains__(self, other)  a2 in a1
(*args, ...) Llamando      __call__(self, *args, **kwargs)    a1(*args, **kwargs)
"""    

"""
Lo mismo que contructores y para imprimir tenemos entre otros:

Función    Método    Expresión
Casting a int        __int__(self)                int(a1)
Función absoluta     __abs__(self)                abs(a1)
Casting a str        __str__(self)                str(a1)
Representación de cuerdas   __repr__(self)        repr(a1)
Casting a bool        __nonzero__(self)            bool(a1)
Formato de cadena     __format__(self, formatstr)    "Hi {:abc}".format(a1)
Hash                  __hash__(self)                hash(a1)
Longitud              __len__(self)                len(a1)
Invertido             __reversed__(self)            reversed(a1)
Piso                  __floor__(self)                math.floor(a1)
Techo                 __ceil__(self)                math.ceil(a1)
También existen los métodos especiales __enter__ y __exit__ para administradores de contexto, y muchos más.
"""
    