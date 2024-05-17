def mezcla_equilibrada(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def ordenamiento_mezcla_equilibrada(arr, tamaño_bloque):
    if tamaño_bloque >= len(arr):
        return sorted(arr)

    bloques_ordenados = [sorted(arr[i:i + tamaño_bloque]) for i in range(0, len(arr), tamaño_bloque)]

    while len(bloques_ordenados) > 1:
        nuevos_bloque_ordenados = []

        for i in range(0, len(bloques_ordenados), 2):
            if i + 1 < len(bloques_ordenados):
                nuevos_bloque_ordenados.append(mezcla_equilibrada(bloques_ordenados[i], bloques_ordenados[i + 1]))
            else:
                nuevos_bloque_ordenados.append(bloques_ordenados[i])

        bloques_ordenados = nuevos_bloque_ordenados

    return bloques_ordenados[0]

arr = [38, 27, 43, 3, 9, 82, 10]
bloque = 3
print("Lista original:", arr)
arreglo_ordenado = ordenamiento_mezcla_equilibrada(arr, bloque)
print("Lista ordenada:", arreglo_ordenado)
