def bubblesort(lista):
    flag = False
    for i in range(len(lista)):
        if (i + 1 < len(lista)) and (lista[i] > lista[i + 1]):
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux
            flag = True
            if flag == False:
                break 
    return lista

'''l = [5, 2, 9, 7]
print(bubblesort(l))'''

l = [("Carlos"), ("Joao"), ("Cris")]
print(bubblesort(l))
