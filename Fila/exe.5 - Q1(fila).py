from fila import Fila

def compara(F1, F2):
  if F1.tamanho == F2.tamanho:
    for v in range(F1.tamanho):
      for v in range(F2.tamanho):
        if F1 == F2:
          print(F1, F2)







F1 = Fila()

for i in range(4):
                                         F1.insere(i)
print(F1)


F2 = Fila()

for i in range(4):
                                         F2.insere(i)
print(F2)

compara(F1,F2)
