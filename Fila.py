class Nodo:
    def __init__(self, dado = 0, proximo_nodo = None):
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
