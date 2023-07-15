"""Base de Datos SQL - Creación de tablas auxiliares"""

from ejercicio_01 import borrar_tabla, crear_tabla

from sqlite3 import connect


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    
    # Completar
    # Creamos la conexion la db
    conn = connect('database.db')
    c = conn.cursor()

    # Creamos la tabla auxiliar
    c.execute(
        '''
        CREATE TABLE PersonaPeso(
            IdPersona INTEGER,
            Fecha DATE,
            Peso INTEGER,
            FOREIGN KEY (IdPersona) REFERENCES Persona(idPersona)
        )
        '''
    )

    # Guardamos y cerramos conexion
    conn.commit()
    conn.close()


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    
    # Completar
    # Creamos la conexion la db
    conn = connect('database.db')
    c = conn.cursor()

    # Creamos la tabla auxiliar
    c.execute(''' DROP TABLE IF EXISTS PersonaPeso ''')

    # Guardamos y cerramos conexion
    conn.commit()
    conn.close()

# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
