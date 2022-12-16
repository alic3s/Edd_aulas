#QUICK SORT
#exemplo aula
def quicksort(lista, inicio, fim):
    if(inicio<fim):
        posicao = particao(lista, inicio, fim)
        quicksort(lista, inicio, (posicao-1))
        quicksort(lista, (posicao + 1), fim)
    return lista

def particao(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[i] <= pivo:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            i+=1
    aux = lista[i]
    lista[i] = lista[fim]
    lista[fim] = aux
    return i

l1 = [5, 2, 9, 7]
print(quicksort(l1, 5, 7))


#exemplo google
# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
