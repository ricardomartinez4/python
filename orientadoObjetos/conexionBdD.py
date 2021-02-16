# -*- coding: utf-8 -*-
"""
Conexión con la base de datos.
"""
import MySQLdb
import keyring
class conectaMySQL():
    
    def __init__(self,username, host, db,passwd):
        return MySQLdb.connect(host=host, username=username, passwd=passwd, db=db)
    def insertar(self):
        sql = "INSERT INTO {}"
    def modificar(self):
        pass
    def listar(self):
        pass
    def borrar(self):
        pass
    def baseDeDatos(self):
        pass