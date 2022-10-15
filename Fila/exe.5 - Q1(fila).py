'''Questão 01. Dado duas filas F1 e F2 que armazenam números inteiros, faça um programa
que tenha as seguintes funções:
+Uma função para testar se as duas filas são iguais (em tamanho e conteúdo). Caso
não sejam iguais, em tamanho, informe qual fila é maior.
+Uma função para retornar o número de elementos de uma fila que possuem valor
ımpar.
+Uma função para retornar o número de elementos da uma fila que possuem valor
par.
Obs. As operações devem ser realizadas sem alteração da fila (sem inserção e remoção).'''

def compare(self, F2):
        if self.tamanho != F2.tamanho:
                if self.tamanho > F2.tamanho:
                        return 'A fila 1 é a maior'
                else:
                        return 'A fila 2 é a maior'
        else:
                print('As filas possuem o mesmo tamanho')
                atual1 = self.cabeca
                atual2 = F2.cabeca
                while atual1 != None:
                        if atual1.dado != atual2.dado:
                                return False
                        atual1 = atual1.proximo
                        atual2 = atual2.proximo
                        return True
                

F1 = Fila()

F1.insere(1)
F1.insere(2)
F1.insere(3)
F1.insere(4)

print(F1)

F2 = Fila()

F2.insere(1)
F2.insere(2)
F2.insere(3)

print(F1.compare(F2))
