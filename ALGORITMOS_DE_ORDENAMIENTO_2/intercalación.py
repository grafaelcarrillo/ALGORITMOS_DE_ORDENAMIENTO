def intercalacion (arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    r = []
    i = 0
    j = 0 
    
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            r.append(arr1[i])
            i += 1
        else:
            r.append(arr2[j])
            j += 1

    while i < n:
        r.append(arr1[i])

    while j < m:
        r.append(arr2[j])
        j += 1

    return r

arreglo1 = [2, 4, 5, 12, 30, 45, 55]
arreglo2 = [23, 34, 56, 67, 89, 120]

print(f"Arreglo 1: {arreglo1}")
print(f"Arreglo 2: {arreglo2}")
print(f"Arreglo Resultado: {intercalacion(arreglo1, arreglo2)}")