#Considere uma pilha P vazia e uma fila F não vazia. Utilizando apenas fila e pilha vazias, e as operações insere e remove. 
#Escreva uma função que inverta a ordem doselementos da fila.

from fila import Fila

from pilha import Pilha

Pilha1 = Pilha()

Fila1 = Fila()

Fila2 = Fila()

Fila1.insere(7)
Fila1.insere(5)
Fila1.insere(3)

print(Fila1)

while not Fila1.vazia():
  temp = Fila1.remove()
  Pilha1.insere(temp)

while not Pilha1.vazia():
  temp2 = Pilha1.remove()
  Fila2.insere(temp2)

print(temp)
print(temp2)
print(Fila2)                              
