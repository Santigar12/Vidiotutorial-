import sqlite3 as sql

def createDB():
    conn = sql.connect("PrimerBaseDeDatos.db")
    conn.commit()
    conn.close()
<<<<<<< HEAD
#createDB()
=======
createDB()
>>>>>>> rama1

def createTable():
    conn = sql.connect("PrimerBaseDeDatos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE alumno(
        name text,
        edad integer
        )"""
    )
    conn.commit()
    conn.close()
<<<<<<< HEAD
createTable()
=======
#createTable()
>>>>>>> rama1


def InsertRow(nombre,edad):

    conn = sql.connect("PrimerBaseDeDatos.db")
    cursor = conn.cursor()
    
    consulta = f"INSERT INTO alumno VALUES('{nombre}', '{edad}')"
    cursor.execute(consulta)

    conn.commit()
    conn.close()





  
