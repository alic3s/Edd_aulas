#MERGE SORT
#exemplo aula
def mergesort(lista, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2
        mergesort(lista, inicio, fim)
        mergesort(lista, meio + 1, fim)
        unir(lista, inicio, meio, fim)
    return lista

def unir(lista, inicio, meio, fim):
    subseq = lista[inicio:meio]
    subdir = lista[meio:fim]

    i=0
    j=0

    for k in range(inicio, fim):
        if i >= len(subseq):
            lista[k] = subdir[j]
            j+=1
        elif j >= len(subdir):
            lista[k] = subseq[i]
            i+=1
        elif subseq[i]<subdir[j]:
            lista[k] = subseq[i]
            i+1
        k+=1

l1 = [5, 2, 9, 7]
print(mergesort(l1, 5, 7))

#exemplo google
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)
