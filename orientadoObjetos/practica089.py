"""
Clases abstractas en Python
(https://www.analyticslane.com/2020/10/05/clases-abstractas-en-python/)
Un concepto importante en programación orientada a objetos es el de las clases abstractas. 
Unas clases en las que se pueden definir tanto métodos como propiedades, pero que no pueden ser instancias directamente. 
Solamente se pueden usar para construir subclases. 
Permitiendo así tener una única implementación de los métodos compartidos, evitando la duplicación de código. 

Otra característica de estas clases es que no es necesario que tengan una implementación de todos los métodos necesarios. 
Pudiendo ser estos abstractos. 

        Los métodos abstractos son aquellos que solamente tienen una declaración, pero no una implementación detallada de las funcionalidades.

Las clases derivadas de las clases abstractas debe implementar necesariamente todos los métodos abstractos para poder crear una clase que se ajuste a la interfaz definida. 
En el caso de que no se defina alguno de los métodos no se podrá crear la clase.

Resumiendo, las clases abstractas define una interfaz común para las subclases. 
Proporciona atributos y métodos comunes para todas las subclases evitando así la necesidad de duplicar código. 
Imponiendo además lo métodos que deber ser implementados para evitar inconsistencias entre las subclases.
"""

"""
A decorator indicating abstract methods.

Requires that the metaclass is ABCMeta or derived from it.  A
class that has a metaclass derived from ABCMeta cannot be
instantiated unless all of its abstract methods are overridden.
The abstract methods can be called using any of the normal
'super' call mechanisms.

Usage:

    class C(metaclass=ABCMeta):
        @abstractmethod
        def my_abstract_method(self, ...):
            ...
"""

from abc import ABC, abstractmethod

#
#
# EL ABC es el que permita que esto funciono pues no heredamos de Object sino de ABC que a  su vez heredará de object
#
class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def comer(self):
        print('Animal come')

        
class Felino(Animal):
    def mover(self):
        print('Mover felino')

    def comer(self):
        # Podemos hacer que se ejecute primero el método abstracto de la clase de la que se hereda
        super().comer()
        print('Felino come')

class Gato(Felino):
    pass

"""        
class Dog(Animal):
    pass
"""
g = Felino()
g.mover()
g.comer()
gt = Gato()
gt.mover()
gt.comer()
"""
print('------------->Aquí tenemos error porque no tenemos definidas los métodos abstractos mover y comer de Animal ')
p = Dog()
"""