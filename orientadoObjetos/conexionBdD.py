# -*- coding: utf-8 -*-
"""
Conexión con la base de datos.
"""
import MySQLdb
class conectaMySQL():
    __bd = None  
    def __init__(self,username, host, database,passwd):
        if not (self.__class__.__bd):
            self.__class__.__bd = MySQLdb.connect(host=host, user=username, passwd=passwd, db=database)
    def insertar(self,tabla,diccionario):
        sql = "INSERT INTO " + tabla + "("
        for campo in diccionario.keys():
            sql += campo + ","
        sql = sql[0:-1] + ") values("
        for valor in diccionario.values():
            sql += "'" + valor + "',"
        sql = sql[0:-1] + ");"
        cur = self.__class__.__bd.cursor()
        cur.execute(sql)
        cur.close()
        self.__class__.__bd.commit()
    def modificar(self,tabla,diccionario,pk):
        sql = "Update " + tabla + " set "
        for campo,valor in diccionario.items():
            sql += campo + " = '" + valor + "',"
        sql = sql[0:-1] + " where " + tabla + "ID = " + pk + ";"
        print(sql)
        cur = self.__class__.__bd.cursor()
        cur.execute(sql)
        self.__class__.__bd.commit()
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
        self.__class__.__bd.commit()
        cur.close()
    def conocerCampos(self,tabla):
        totalCampos = []
        sql = "SHOW COLUMNS FROM " + tabla + ";"
        cur = self.__class__.__bd.cursor()
        cur.execute(sql)
        todos = cur.fetchall()
        for row in todos:
            if(row[0]== tabla + 'ID'):
                continue 
            else:
                totalCampos.append(row[0])
        self.__class__.__bd.commit()
        cur.close()
        return totalCampos  
try:
    dataBase = input("Database que vas a usar: ")
    conexion = conectaMySQL("ricardomartinez4","localhost",dataBase,"1234")
    while(True):
        print("1 - INSERTAR")
        print("2 - MODIFICAR")
        print("3 - LISTAR")
        print("4 - BORRAR")
        print("5 - SALIR")
        opcion = input("Inserte la opcion que desea realizar: ")
        assert opcion=="1" or opcion=="2" or opcion=="3" or opcion=="4" or opcion=="5", "OPCION NO VÁLIDA"
        if (opcion=="1"):
            tabla = input("Tabla que desea introducir valores: ")
            conocer = conexion.conocerCampos(tabla)
            print("Campos que tiene {}: {}".format(tabla,conocer))
            diccionario = {}
            for x in conocer:
                if(x[-2:] == 'ID'):
                    listado = conexion.listar(x[:-2])
                    print("Valores de la tabla {}: {}".format(x[:-2],listado))
                    diccionario[x] = input("Introduce el valor que desea introducir en {}: ".format(x))
                else:
                    diccionario[x] = input("Introduce el valor que desea introducir en {}: ".format(x))
            insertar1 = conexion.insertar(tabla, diccionario)
        elif(opcion == "2"):
            tabla = input("Tabla que desea modificar: ")
            listado = conexion.listar(tabla)
            print(listado)
            pk = input("Identificador de la fila que desea modificar: ")
            conocer = conexion.conocerCampos(tabla)
            print("Campos que tiene {}: {}".format(tabla,conocer))
            campo = input("Campo que desea modificar: ")
            diccionario = {}
            for x in conocer:
                if(x==campo):
                    diccionario[x] = input("Introduce el valor que desea introducir en {}: ".format(x))
            modificar1 = conexion.modificar(tabla, diccionario,pk)
        elif(opcion=="3"):
            tabla = input("Tabla que desea visualizar: ")
            print(conexion.listar(tabla))
        elif(opcion == "4"):
            tabla = input("Tabla de la que desea borrar valores: ")
            listado = conexion.listar(tabla)
            print(listado)
            pk = input("Identificador del elemento que desea borrar: ")
            borrar1 = conexion.borrar(tabla, pk)
            print("Ha sido borrado con éxito!")
        elif(opcion=="5"):
            print("Hasta pronto!")
            break   
except Exception as e:
    print(e)