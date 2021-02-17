# -*- coding: utf-8 -*-
"""
Conexión con la base de datos.
"""
import MySQLdb

class conectaMySQL():
    __bd = None
    
    def __init__(self,username, host, db,passwd):
        if not (self.__class__.__bd):
            self.__class__.__bd = MySQLdb.connect(host=host, username=username, passwd=passwd, db=db)
    def insertar(self,tabla,diccionario):
        sql = "INSERT INTO " + tabla + "("
        for campo in diccionario.keys():
            sql += campo + ","
        sql += ") values("
        for valor in diccionario.values():
            sql += valor + ","
        sql = sql[0:-1] + ");"
        cur = self.__class__.__bd.cursor()
        cur.execute(sql)
        cur.commit()
        cur.close()
    def modificar(self,tabla,diccionario,pk):
        sql = "Update " + tabla + " set "
        for campo,valor in diccionario.items():
            sql += campo + " = " + valor + ","
        sql = sql[0:-1] + " where " + tabla + "ID = " + pk + ";"
        cur = self.__class__.__bd.cursor()
        cur.execute(sql)
        cur.commit()
        cur.close()
    def listar(self,tabla):
        sql = "Select * from " + tabla + ";"
        cur = self.__class__.__bd.cursor()
        cur.execute(sql)
        return cur.fetchall()
    def borrar(self,tabla,pk):
        sql = "DELETE FROM " + tabla + " WHERE " + tabla + "ID = " + pk + ";" 
        cur = self.__class__.__bd.cursor()
        cur.execute(sql)
        cur.commit()
        cur.close()
