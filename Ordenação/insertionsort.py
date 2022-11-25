def insertionsort(lista):
    for  i in range(1, len(lista)):
        j = i - 1
        while j >= 0 and lista[j] > lista[i]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            j -= 1
    return lista

l = [5, 2, 9, 7]
print(insertionsort(l))
