#SELECTION SORT
#exemplo aula
def selectionsort(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

l = [5, 2, 9, 7, 1, 0, 56, 78]
print(selectionsort(l))

l2 = [("Carlos",70), ("Joao",20), ("Cris",40), ("Alice", 10), ("Alane", 25)]
print(selectionsort(l2))


#exemplo google
def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-9, 3, -10, 45, 8]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
