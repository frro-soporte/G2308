"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

import os

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    # Completar

    # Conexion con la DB
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Creamos la tabla en la DB
    c.execute(
        """
        CREATE TABLE
            Persona(
                idPersona INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre CHAR(30),
                FechaNacimiento DATE,
                DNI INTEGER,
                Altura INTEGER
            )
        """
    )

    # Cerrar la conexión
    conn.close()

       

def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""



    # Completar
    # Conexion con la DB
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Eliminamos la tabla en la DB
    c.execute(""" DROP TABLE IF EXISTS PERSONA """)

    # Cerrar la conexión
    conn.close()



# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
