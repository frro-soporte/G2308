"""Base de Datos SQL - Baja"""

import datetime

import sqlite3

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    
    
    # Completar
    # Creamos conexion con la db
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Eliminamos la Persona
    c.execute(
        'DELETE FROM Persona WHERE idPersona = ?', (id_persona,)   # OJO la forma de pasar los parametros
    )

    # Guardamos 
    registro_eliminado = c.rowcount > 0

    # Confirmamos y cerramos conexion
    conn.commit()
    conn.close()

    # Devolvemos si eliminamos el registro
    return registro_eliminado


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert borrar_persona(id)
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN