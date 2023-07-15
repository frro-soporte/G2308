"""Any y Sets."""

from typing import Any, Iterable

def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Toma dos listas y devuelve un booleano en base a si tienen al menos 1
    elemento en común.
    Restricción: Utilizar bucles anidados.
    """
    
    
    # Completar
    for l1 in lista_1:
        for l2 in lista_2:
            if l1 == l2:
                return True
    return False


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_basico(test_list, (2, "world", 35.20))
assert not superposicion_basico(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_in(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando un sólo bucle y el operador IN."""
    
    
    # Completar
    for l1 in lista_1:
        if l1 in lista_2:
            return True
    return False


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_in(test_list, (2, "world", 35.20))
assert not superposicion_in(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando sin bucles, el operador in y la funcion any.
    Referencia: https://docs.python.org/3/library/functions.html#any
    """
    
    
    # Completar
    # Funcion any -> verifica si uno de los elemnetos del iterable es True. any([False, False, True, ...])
    # Funcion map -> Aplica a cada elemento de la lista una funcion. map(funcion, iterable)
    return any(map(lambda x: x in lista_2, lista_1))


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_any(test_list, (2, "world", 35.20))
assert not superposicion_any(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando conjuntos (sets).
    Referencia: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
    """
    
    
    # Completar

    """Primero, convertimos las dos listas en conjuntos usando la función set. 
    Luego, utilizamos la operación de intersección '&' para obtener un conjunto 
    que contiene los elementos que están presentes en ambos conjuntos. 
    Finalmente, convertimos el conjunto resultante en un valor booleano utilizando la función bool. 
    Devuelve True si el conjunto no está vacío (es decir, si hay elementos en común), y False en caso contrario."""
    set_1 = set(lista_1)
    set_2 = set(lista_2)
    return bool(set_1 & set_2)


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_set(test_list, (2, "world", 35.20))
assert not superposicion_set(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN