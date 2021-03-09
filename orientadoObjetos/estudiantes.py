"""
Herencia múltiple
"""
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return "Nombre: " + self.nombre 
    
    @property
    def nombre(self):
        return self.__nombre
    # setters
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
class Asignatura():
    def __init__(self,asignatura):
        self.__asignatura = asignatura
    def __str__(self):
        return "Asignatura: {}".format(self.__asignatura)
    @property
    def asignatura(self):
        return self.__asignatura
class Curso():
    def __init__(self,curso):
        self.__curso = curso
    def __str__(self):
        return "Curso: {}".format(self.__curso)
    @property
    def curso(self):
        return self.__curso
class Profesor(Persona):
    def __init__(self,profesor):
        Persona.__init__(self, profesor)
    def __str__(self):
        return "Profesor: {}".format(Persona.__str__(self))
    @property
    def profesor(self):
        return self.__profesor
class AsignaturaCurso():
    def __init__(self,profesor,curso,asignatura):
        assert(isinstance(profesor, Profesor)), "No es instancia de profesor"
        assert(isinstance(curso, Curso)),"No es instancia de curso"
        assert(isinstance(asignatura, Asignatura)),"No es instancia de asignatura"
        self.__profesor = profesor
        self.__curso = curso
        self.__asignatura = asignatura
    @property
    def profesor(self):
        return self.__profesor.profesor
    @property
    def curso(self):
        return self.__curso.curso
    @property
    def asignatura(self):
        return self.__asignatura.asignatura

class Notas():
    # constructor
    def __init__(self):
        self._notas={}
    
    @property
    def notas(self):
        resultado=""
        for key,value in self._notas.items():
            resultado+=key+": "+str(value)+"\n"
        return resultado
    
    # métodos:
    def addnotas(self,asig,nota):
        assert(isinstance(asig, Asignatura)), "La asignatura no esta creada"
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
            resultado+=key+": "+str(value)+"\n"
        return resultado
    
class Alumno(Persona, Notas):
    __instancias = []
    def __init__(self, nombre):
        Persona.__init__(self, nombre)
        Notas.__init__(self)
        Alumno.__instancias.append(self)
        
    def __str__(self):
        return Persona.__str__(self)+"\n"+Notas.__str__(self)
    @classmethod
    def cuantasInstancias(cls):
        return cls.__instancias
    @classmethod
    def verNotas(cls,profesor):
        assert(isinstance(profesor, Profesor)),"El profesor debe ser instancia de profesor"
        for alumno in cls.__instancias:
            print(alumno.nombre)
            for entrada in alumno._notas.keys():
                if(entrada.profesor == profesor.profesor):
                    print('hola')
            
try:
    persona = Persona('Juan Antonio Estuardo')
    print(persona)

    alumnPaco = Alumno('Paco Pérez González')
    print(alumnPaco)
  
    alumnPaco.addnotas('Programación', 6)
    alumnPaco.addnotas('Marcas', 6.5)
    print('Media: ' + str(alumnPaco.media()))
    #
    print("-"*80)
    #
    alumno = Alumno('Antonio Salmerón Cerdá')
    alumno.addnotas('Programación', 5)
    alumno.addnotas('Entornos', 5.3)
    print(alumno)
    print('Media: ' + str(alumno.media()))
    #
    
    #
    print("-"*80)
   
    print('------------- Orden de resolución------------------')
    print(Alumno.mro())
    print('---------------- listamos todos los miembros de la clase alumno--------------------')
    print([m for m in dir(alumno) if not m.startswith('__')])
    
    
except Exception as e:
    print("Error: " + str(e))