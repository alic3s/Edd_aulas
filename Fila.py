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

    def __repr__(self):
        return '[' + str(self.cabeca) + ']'

    def vazia(self):
        if self.cabeca == None:
            return True
        else:
            return False
    
    def insere(self, novo_dado):
        novo_nodo = novo_dado
        if 
