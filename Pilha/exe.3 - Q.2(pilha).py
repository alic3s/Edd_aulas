#Considere uma pilha que armazena caracteres. Faça uma função para determinar se uma string é da forma XY, onde X é uma cadeia formada por caracteres
#arbitrários e Y é o reverso de X. Por exemplo, se x = ABCD, então y = DCBA. Considere que x e y são duas strings distintas.

#É uma função

def padraoXY(string):
  if len(string) %2 != 0:
    return False
  else:
    string1 = string[:len(string)//2]
    string2 = string[len(string)//2:]
    pilha = Pilha()
    for letra in string1:
      pilha.insere(letra)
      for letra in string2:
        if letra != pilha.remove():
          return False
        return True
