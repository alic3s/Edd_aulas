class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'


class Fila:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def __repr__(self):
        return '[' + str(self.cabeca) + ']'

    def vazia(self):
        if self.cabeca == None:
            return True
        else:
            return False

    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        self.tamanho += 1
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
        else:
            self.cauda.proximo = novo_nodo
            self.cauda = novo_nodo

    def remove(self):
        removido = self.cabeca.dado
        self.cabeca = self.cabeca.proximo
        self.tamanho -= 1
        if self.cabeca == None:
            self.cauda = None
        return removido

    def compare(self, F2):
        if self.tamanho != F2.tamanho:
            return False
        else:
            atual1 = self.cabeca
            atual2 = F2.cabeca
            while atual1 != None:
                if atual1.dado != atual2.dado:
                    return False
                atual1 = atual1.proximo
                atual2 = atual2.proximo
            return True

fila = Fila()

for i in range(5):
    fila.insere(i)
print(fila)

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
