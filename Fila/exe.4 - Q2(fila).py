#Faça uma função que receba duas filas já preenchidas em ordem crescente e retorne uma terceira fila com os valores das duas primeiras em ordem crescente.
from pilha import Pilha
from fila import Fila

Fila1 = Fila()

for i in range(1, 9, 2):
  Fila1.insere(i)
print(Fila1)

Fila2 = Fila()

for i in range(0, 9, 2):
  Fila2.insere(i)
print(Fila2)


Fila3 = Fila()

while not Fila1.vazia() and not Fila2.vazia():
  if Fila1.cabeca.dado <= Fila2.cabeca.dado:
    Fila3.insere(Fila1.remove())
    else:
      Fila3.insere(Fila2.remove())
      
while not Fila1.vazia():
  Fila3.insere(Fila1.remove())
  
while not Fila2.vazia():
  Fila3.insere(Fila2.remove())

print(Fila3)
