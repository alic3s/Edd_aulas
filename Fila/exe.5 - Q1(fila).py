'''Questão 01. Dado duas filas F1 e F2 que armazenam números inteiros, faça um programa
que tenha as seguintes funções:
+Uma função para testar se as duas filas são iguais (em tamanho e conteúdo). Caso
não sejam iguais, em tamanho, informe qual fila é maior.
+Uma função para retornar o número de elementos de uma fila que possuem valor
ımpar.
+Uma função para retornar o número de elementos da uma fila que possuem valor
par.
Obs. As operações devem ser realizadas sem alteração da fila (sem inserção e remoção).'''

from classe_fila import Fila

def compare(F1, F2):
        if F1.tamanho != F2.tamanho:
                if F1.tamanho > F2.tamanho:
                        return 'A fila 1 é a maior'
                else:
                        return 'A fila 2 é a maior'
        else:
                print('As filas possuem o mesmo tamanho')
                atual1 = F1.cabeca
                atual2 = F2.cabeca
                while atual1 != None:
                        if atual1.dado != atual2.dado:
                                return 'Os conteúdos são diferentes.'
                        atual1 = atual1.proximo
                        atual2 = atual2.proximo
                        return 'Os conteúdos são iguais.'

                
            
        
        
def contaPar(self):
    par = 0
    atual1 = self.cabeca

    while atual1.dado != None:
        if atual1.dado % 2 == 0:
            par += 1

        atual1 = atual1.proximo
    return par

def contaImpar(self):
    impar = 0
    atual1 = self.cabeca
    while atual1.dado != None:
        if atual1.dado%2 != 0:
            impar += 1

        atual1 = atual1.proximo
    return impar




F1 = Fila()

for i in range(1, 9, 2):
    F1.insere(i)

print(F1)

F2 = Fila()

for i in range(1, 9, 2):
    F2.insere(i)

print(F2)

print(compare(F1,F2))
