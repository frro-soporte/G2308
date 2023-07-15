"""Base de datos SQL - Listar"""

import datetime

from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla
from ejercicio_07 import agregar_peso

from sqlite3 import connect


def listar_pesos(id_persona):
    """Implementar la funcion listar_pesos, que devuelva el historial de pesos 
    para una persona dada.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
     mplementadas).

    Debe devolver:
    - Lista de (fecha, peso), donde fecha esta representado por el siguiente 
    formato: AAAA-MM-DD.

    Ejemplo:
    [
        ('2018-01-01', 80),
        ('2018-02-01', 85),
        ('2018-03-01', 87),
        ('2018-04-01', 84),
        ('2018-05-01', 82),
    ]

    - False en caso de no cumplir con alguna validacion.
    """

    # Creamos la conexion a la DB
    conn = connect('database.db')
    c = conn.cursor()

    if buscar_persona(id_persona): # Validamos que exista la persona
        
        select_pesos = c.execute(    # Guardamos la lista de pesos de la persona con Fecha y Peso
            '''
            SELECT
                Fecha,
                Peso
            FROM
                PersonaPeso
            WHERE
                IdPersona = ?
            ''', (id_persona,)
        )

        # Inicializamos la lista y guardamos cada valor del SELECT
        listaPesos = [(datetime.datetime.strptime(fila[0], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"), fila[1]) for fila in select_pesos]

        # Cerramos la conexion
        conn.close()

        # Devolvemos la lista de pesos
        return listaPesos
    
    # Si la persona no existe cerramos la conexion y devolvemos False
    conn.close()
    return False

    


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN