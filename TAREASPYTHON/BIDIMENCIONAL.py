# Matriz bidimensional 3*3.

matriz = [
    [1, 2, 3],
    [2, 8, 1],
    [3, 9, 4]
]

# Valor que se busca
valor_buscado = 4

# variables en que se busca
fila_buscada = -1
columna_buscada = -1

#
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_buscada = fila
            colmna_buscada = columna

            break  # Detener la busqueda al encontrar el número
    if fila_buscada != 0:

        break  # Salir al encontrar el valor.

# Revisar si se encontró y la posicion del numero encontrado
if fila_buscada != 0:
    print(f" encontrado el (valor_buscado) en la fila (fila_buscada)y columna (columna buscada) ")
else:
    print(f"(valor_buscado no se encontro en la matriz.")




