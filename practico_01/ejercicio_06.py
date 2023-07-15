"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union

def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    
    
    # Completar
    num = []
    letra = []
    for l in lista:
        if type(l) == int:
            num.append(l)
        else:
            letra.append(l)
    return letra + num
    

# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""
    
    
    # Completar
    num = []
    letra = []
    for l in lista:
        num.append(l) if type(l) == int else letra.append(l)
    return letra + num


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    
    
    # Completar
    resp = sorted(lista, key = lambda x: isinstance(x, str), reverse = True)
    return resp


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    
    # Completar
    num = list(filter(lambda x: type(x) == int, lista))           #Diferentes formas de comparar el type
    letra = list(filter(lambda x: isinstance(x, str), lista))
    return letra + num
    

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    
    
    # if not lista:  # Empty list
    #     return []
    # elif isinstance(lista[-1], str):  # Primer elemento un string
    #     return [lista[-1]] + numeros_al_final_recursivo(lista[:-1])
    # else:  # Primer elemento un numero
    #     return numeros_al_final_recursivo(lista[:-1]) + [lista[-1]]

    # if not lista:  # Base case: empty list
    #     return []
    # elif isinstance(lista[0], str):  # First element is a string
    #     return [lista[0]] + numeros_al_final_recursivo(lista[1:])
    # else:  # First element is a number
    #     return numeros_al_final_recursivo(lista[1:]) + [lista[0]]


# # NO MODIFICAR - INICIO
# if __name__ == "__main__":
    # print(numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]))
    # assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# # NO MODIFICAR - FIN