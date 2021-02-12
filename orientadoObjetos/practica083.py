"""
múltiples constructores. 
es una simulación---> otros lenguajes de programación si permiten más de un constructor de la clase
aquí lo hacemos mediante métodos de clase
"""
class Person():
    
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.full_name = nombre + " " + apellidos
    
    # No tenemos en cuenta los nombres o apellidos compuestos
    @classmethod
    def from_full_name(cls, nombreCompleto, edad):
        assert(" " in nombreCompleto), ValueError
        # string.split(separator, maxsplit)  maxsplit is Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
        nombre, apellidos = nombreCompleto.split(" ", 2)
        # Ahora llamamos al constructor de la clase
        return cls(nombre, apellidos, edad) 
        
    def saludo(self):
        return "Hola mi nombre es " + self.full_name + "."
        
try:
    print(Person("Antonio", "López", 32).saludo())
    print(Person.from_full_name("Antonio Gutiérrez", 32).saludo())
    
except Exception as e:
    print("Error: " + str(e))