def selectionsort(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

l = [5, 2, 9, 7]
print(selectionsort(l))
