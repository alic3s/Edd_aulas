def insertionsort(lista):
    for  i in range(1, len(lista)):
        escolhido = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > lista[i]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            j -= 1
            i -= 1
        lista[j + 1] = escolhido
    return lista

l = [5, 2, 9, 7, 12, 10, 25, 22]
print(insertionsort(l))
