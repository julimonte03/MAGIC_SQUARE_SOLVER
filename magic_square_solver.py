# A magic square of order n is a square arrangement of the numbers {1, ..., n^2} such that the sum of each row, each column, and both diagonals is the same (see figure). The number that each row sums to is called the magic number.

# 2 7 6
# 9 5 1
# 4 3 8

# There are many methods to generate magic squares. The objective of this exercise is to count how many magic squares of order n exist.

def cuantos_cuadrados_magicos(n):
    if n < 1:
        return 0

    matriz = [[0] * n for _ in range(n)]
    valores_disponibles = set(range(1, n * n + 1))
    fila_sumas = [0] * n
    columna_sumas = [0] * n
    diagonal1_suma = 0
    diagonal2_suma = 0
    
    return contar_cuadrados_magicos(matriz, 0, valores_disponibles, fila_sumas, columna_sumas, diagonal1_suma, diagonal2_suma)

def contar_cuadrados_magicos(matriz, posicion_actual, valores_disponibles, fila_sumas, columna_sumas, diagonal1_suma, diagonal2_suma):
    n = len(matriz)

    # verifico si llegue a la ultima posicion
    if posicion_actual == n * n:
        magic_number = sum(range(1, n * n + 1)) // n
        for i in range(n):
            if fila_sumas[i] != magic_number or columna_sumas[i] != magic_number:
                return 0
        if diagonal1_suma != magic_number or diagonal2_suma != magic_number:
            return 0
        return 1
    
    # cada posicion lineal tiene una posicion en forma de tupla
    fila = posicion_actual // n
    columna = posicion_actual % n

    # backtracking: por cada posicion me voy a fijar, con cada valor disponible si es una matriz valida(recursivamente), es decir si cumple con las restricciones. Para eso saco el valor de valores_disponibles y me fijo recursivamente si es valida la matriz con los demas valores en las otras posiciones. Una vez que ya tengo la cuenta de las matrices posibles con ese valor en esa posicion, lo vuelvo a agregar a la lista y sigo con el siguiente
    count = 0
    for valor in valores_disponibles:
        if es_valida(matriz, fila_sumas, columna_sumas, diagonal1_suma, diagonal2_suma, (fila, columna), valor):
            matriz[fila][columna] = valor
            fila_sumas[fila] += valor
            columna_sumas[columna] += valor
            if fila == columna:
                diagonal1_suma += valor
            if fila + columna == n - 1:
                diagonal2_suma += valor

            valores_disponibles.remove(valor)
            count += contar_cuadrados_magicos(matriz, posicion_actual + 1, valores_disponibles, fila_sumas, columna_sumas, diagonal1_suma, diagonal2_suma)
            valores_disponibles.add(valor)
            matriz[fila][columna] = 0
            if fila == columna:
                diagonal1_suma -= valor
            if fila + columna == n - 1:
                diagonal2_suma -= valor
            fila_sumas[fila] -= valor
            columna_sumas[columna] -= valor

    return count

def es_valida(matriz, fila_sumas, columna_sumas, diagonal1_suma, diagonal2_suma, posición, valor):
    fila = posición[0]
    columna = posición[1]
    
    # Verificacion de que las sumas parciales no excedan lo posible en esa fila/columna/diagonal
    magic_number = sum(range(1, len(matriz) * len(matriz) + 1)) // len(matriz)

    if fila_sumas[fila] + valor > magic_number or columna_sumas[columna] + valor > magic_number:
        return False
    if fila == columna and diagonal1_suma + valor > magic_number:
        return False
    if fila + columna == len(matriz) - 1 and diagonal2_suma + valor > magic_number:
        return False
    
    return True

# Ejemplo:
n = 3
print(f"Cantidad de cuadrados mágicos de orden {n}: {cuantos_cuadrados_magicos(n)}")
