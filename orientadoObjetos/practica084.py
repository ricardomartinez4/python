"""
Alumno. Herencia múltiple de Persona y Notas
"""

class Dni():

    def __init__(self, numero):
        self.numero=numero

    def __str__(self):
        return "{0}-{1}".format(self.numero,self.letra)
    
    # getters
    @property
    def numero(self):
        return self.__numero
    
    @property
    def letra(self):
        return self.__letra
    
    @classmethod
    def devuelveLetra(cls, numero):
        # cls: Hace referencia a la clase, es un método de clase
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return letras[int(numero)%23]

    # setter
    @numero.setter
    def numero(self,numero):
        if (len(numero)==9):
            self.__numero = numero[0:len(numero)-1]
        else: 
            self.__numero = numero
        assert((len(self.__numero)==9 or (len(self.__numero)==8)) and self.__numero.isdigit()), "DNI " + numero + " incorrecto (Número no válido)"
        # Aquí llamamos a calcular la letra, llamamos al método de clase:
        self.__letra = Dni.devuelveLetra(self.__numero)
        #
        assert((len(self.__numero)==8) or (len(self.__numero) == 9 and self.__letra == numero[-1])),  "DNI " + numero + " incorrecto (letra no válida)"

class Persona():
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.__dni = Dni(numero)
    def __str__(self):
        return "Nombre: " + self.nombre + " con dni " + str(self.dni)
    
    # getters
    @property
    def dni(self):
        return self.__dni
    @property
    def nombre(self):
        return self.__nombre
    # setters
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        

class Notas():
    # constructor
    def __init__(self):
        self._notas={}
    
    @property
    def notas(self):
        resultado=""
        for key,value in self._notas.items():
            resultado+=key+":"+str(value)+"\n"
        return resultado
    
    # métodos:
    def addnotas(self,asig,nota):
        self._notas[asig]=nota

    def modnota(self,asig,nota):
        if asig in self._notas.keys():
            self._notas[asig]=nota
        else:
            raise ValueError("Asignatura incorrecta")

    def delnota(self,asig):
        if asig in self._notas.keys():
            del self._notas[asig]
        else:
            raise ValueError("Asignatura incorrecta")

    def media(self):
        if (len(self._notas.values()) > 0):
            return sum(self._notas.values())/len(self._notas.values())
        else:
            raise ValueError("El usuario no tiene ninguna nota")

    def __str__(self):
        resultado=""
        for key,value in self._notas.items():
            resultado+=key+":"+str(value)+"\n"
        return resultado
    
class Alumno(Persona, Notas):

    def __init__(self, nombre, dni):
        Persona.__init__(self, nombre, dni)
        Notas.__init__(self)
        
    def __str__(self):
        return Persona.__str__(self)+"\n"+Notas.__str__(self)

try:
    persona = Persona('Juan Antonio Estuardo', '00000000')
    print(persona)

    alumnPaco = Alumno('Paco Pérez González', '24342989')
    print(alumnPaco)
  
    alumnPaco.addnotas('Programación', 6)
    alumnPaco.addnotas('Marcas', 6.5)
    print('Media: ' + str(alumnPaco.media()))
    #
    print("-"*80)
    #
    alumno = Alumno('Antonio Salmerón Cerdá', '52769781')
    alumno.addnotas('Programación', 5)
    alumno.addnotas('Entornos', 5.3)
    print(alumno)
    print('Media: ' + str(alumno.media()))
    #
    print('------------- dir(Dni)------------------')
    print(dir(Dni))
    #
    print("-"*80)
    print([m for m in dir(Dni) if not m.startswith('__')])
    print('------------- Orden de resolución------------------')
    print(Alumno.mro())
    print('---------------- listamos todos los miembros de la clase alumno--------------------')
    print([m for m in dir(alumno) if not m.startswith('__')])
    
    
except Exception as e:
    print("Error: " + str(e))