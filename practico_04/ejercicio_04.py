"""Base de Datos SQL - Búsqueda"""

import datetime

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona

import sqlite3 


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    
    
    # Completar

    # Conectamos la db
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Buscamos la persona
    c.execute(
        '''SELECT * FROM Persona WHERE idPersona = ?''', (id_persona,)
    )

    persona = c.fetchone()

    # Guardamos y cerramos conexion
    conn.commit()
    conn.close()

    if persona:
        return persona
    return False

    
# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', str(datetime.datetime(1988, 5, 15)), 32165498, 180)  #Tuve que modificar el tipo al datetime
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN