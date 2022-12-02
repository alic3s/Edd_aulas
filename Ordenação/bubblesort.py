#exemplo aula
def bubblesort(lista):
    while True:
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

l1 = [9, 4, 1, 2, 7, 0]
print(bubblesort(l1))

l = [("Carlos",70), ("Joao",20), ("Cris",40), ("Alice", 10)]
print(bubblesort(l))


#exemplo google
'''def bubbleSort(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                troca = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = troca

l1 = [54,26,93,17,77,31,44,55,20]
bubbleSort(l1)
print(l1)'''


#exemplo google
def bubbleSort(lista):
  for i in range(len(lista)):   #loop to access each array element
    for j in range(0, len(lista) - i - 1):   #loop to compare array elements
      if lista[j] > lista[j + 1]:     #compare two adjacent elements // # change > to < to sort in descending order
        # swapping elements if elements
        # are not in the intended order
        temp = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = temp

data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
