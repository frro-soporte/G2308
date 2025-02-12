"""Slicing."""

def es_palindromo(palabra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si se lee igual al
    derecho y al revés.
    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    
    
    # Completar
    return palabra == palabra[::-1]


# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


###############################################################################


def mitad(palabra: str) -> str:
    """Toma un string y devuelve la mitad. Si la longitud es impar, redondear
    hacia arriba.
    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    
    
    # Completar
    # l = len(palabra)/2
    # if ((l % 2) != 0):
    #     return palabra[0 : (int(l)+1)]
    # else:
    #     return palabra[0 : int(l)]

    # if len(palabra) % 2 == 0:
    #     return palabra[ : int(len(palabra) / 2)]
    # return palabra[ : (int(len(palabra) / 2) + 1)]
    
    return palabra[: int(len(palabra) / 2)] if len(palabra) % 2 == 0 else palabra[: (int(len(palabra) / 2) + 1)]
    # Los 3 codigos son similares 


# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
