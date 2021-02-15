# -*- coding: utf-8 -*-
import MySQLdb
import keyring
from conectaBS2 import conectaMySql
from conectaBS3 import devuelveCursor
class entrenadoresDeportes():
    def __init__(self,entrenadoresDeportesID,entrenadorID,deporteID):
        self.__entrenadoresDeportesID = int(entrenadoresDeportesID)
        self.__entrenadorID = int(entrenadorID)
        self.__deporteID = int(deporteID)
    def insertar(self,valorInsertar):
        pass
    def modificar(self,valorModificar):
        pass
    def borrar(self,valorBorrar):
        pass
    def listar(self,valorListar):
        pass
    
class salasDeportes():
    def __init__(self,salasDeportesID,deportesID,salaID,aforo):
        self.__salasDeportesID = int(salasDeportesID)
        self.__deportesID = int(deportesID)
        self.__salaID = int(salaID)
        self.__aforo = int(aforo)
    def insertar(self,valorInsertar):
        pass
    def modificar(self,valorModificar):
        pass
    def borrar(self,valorBorrar):
        pass
    def listar(self,valorListar):
        pass