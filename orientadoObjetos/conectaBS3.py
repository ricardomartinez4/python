from conectaBS2 import conectaMySql

def devuelveCursor(): 
        # Abrimos la conexión a la base de datos:
    db = conectaMySql("ricardomartinez4", "localhost", "w3schools")
    # Create a Cursor object to execute queries.
    cursor = db.cursor()
    # Select data from table using SQL query.
    return cursor
