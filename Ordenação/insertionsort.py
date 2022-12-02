'''#INSERTION SORT
#exemplo aula
def insertionsort(lista):
    for i in range(1, len(lista)):
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



#exemplo google
def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array

l1 = [5, 2, 9, 7, 12, 10, 25, 22]
print(insertion_sort(l1))'''



#exemplo google
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
