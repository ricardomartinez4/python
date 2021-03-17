# -*- coding: utf-8 -*- 
class Cultivo():
    def __init__(self,tipo,extension):
        self.tipo = tipo
        self.extension = extension
    def __str__(self):
        return "Cultivo de tipo {} y extension {}".format(self.tipo,self.extension)
    @property
    def tipo(self):
        return self.__tipo
    @property
    def extension(self):
        return self.__extension
    @tipo.setter
    def tipo(self,tipo):
        assert tipo==1 or tipo==2 or tipo==3, "Tipo de cultivo no valido!"
        self.__tipo = tipo
    @extension.setter
    def extension(self,extension):
        assert extension > 0 and extension < 500, "Hectáreas no válidas"
        self.__extension = extension
    def productividad(self):
        productividad = 0
        if(self.tipo==1):
            productividad += self.extension*1.1
        elif(self.tipo==2):
            productividad += self.extension*1.55
        elif(self.tipo==3):
            productividad += self.extension*1.36
        return productividad
        
class Ganado():
    def __init__(self,tipo,extension):
        self.tipo = tipo
        self.extension = extension
    @property
    def tipo(self):
        return self.__tipo
    @property
    def extension(self):
        return self.__extension
    @tipo.setter
    def tipo(self,tipo):
        assert tipo==1 or tipo==2 or tipo==3, "Tipo de ganado no valido!"
        self.__tipo = tipo
    @extension.setter
    def extension(self,extension):
        assert extension > 0 and extension < 500, "Hectáreas no válidas"
        self.__extension = extension   
class Finca():
    def __init__(self):
        self.__explotaciones = []
    def imprimeExplotaciones(self):
        for expl in self.__explotaciones:
            print(expl)
    def addExplotacion(self,clase,tipo,extension):
        cult = clase(tipo,extension)
        self.__explotaciones.append(cult)
        return cult
#try:
finca1 = Finca()
olivar = finca1.addExplotacion(Cultivo,2, 410)
print(olivar.productividad())
#except Exception as e:
#    print(e)
    