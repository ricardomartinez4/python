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
    def insertar(self,nuevoEntrenadorID,nuevoDeporteID):
        cursor = devuelveCursor()
        cursor.execute('Insert into entrenadoresdeportes(entrenadorID,deporteID) values ({},{});'.format(nuevoEntrenadorID,nuevoDeporteID))
    def borrar(self,valorBorrar):
        cursor = devuelveCursor()
        cursor.execute('DELETE FROM entrenadoresdeportes WHERE entrenadorID= {};'.format(valorBorrar))
    def listar(self,ordenado):
        cursor = devuelveCursor()
        cursor.execute('SELECT * from entrenadoresdeportes order by {} ;'.format(ordenado))
        todos = cursor.fetchall()
        for valor in todos:
            print(valor)
