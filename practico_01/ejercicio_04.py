"""Expresiones Booleanas."""

def es_vocal_if(letra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si letra es una vocal o
    no.
    Restricción: Utilizar un if para cada posibilidad con la función lower().
    Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods
    """
    

    # Completar
    letra = letra.lower()
    if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
        return True
    return False


# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    """Re-escribir utilizando un sólo IF y el operador IN.
    Referencia: https://docs.python.org/3/reference/expressions.html#membership-test-operations
    """


    # Completar
    letra = letra.lower()
    if letra in ['a','e','i','o','u']:
        return True
    return False


# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    """Re-escribir utilizando el operador IN pero sin utilizar IF."""
    
    
    # Completar
    letra = letra.lower()
    return letra in ['a','e','i','o','u']

    
# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN