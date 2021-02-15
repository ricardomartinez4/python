# -*- coding: utf-8 -*-
'''
Ejemplo de conexión a la base de datos w3schools usando MySQLdb

            sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
            python -m pip install --upgrade pip
'''
import MySQLdb
import keyring

def conectaMySql(username, host, database):
    '''
    Obtenemos una conexión a la base de datos mySql en el host dado para el usuario suministrado
        username: Usuario en nombre del cual abrimos la conexión
        host: Server en el que se encuentra la base de datos
        database: Base de datos a la que nos queremos conectar
    Devuelve una conexión a la base de datos
    '''
    return MySQLdb.connect(host=host, 
                     user= username,
                     passwd= keyring.get_password("mysql", username),
                     db=database)