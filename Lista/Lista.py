class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'

class Lista:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
    
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    
    def vazia(self):
        if (self.cabeca == None):
            return True
        else:
            return False
    
    def insereInicio(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
        else:
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo
        self.tamanho += 1
    
    def insereFim(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
        else:
            self.cauda.proximo = self.cauda
            self.cauda = novo_nodo
        self.tamanho += 1
    
    def remove(self, posicao):
        if self.vazia():
            return f'Impossível remover valor de lista vazia'
        elif (posicao) == 0:    #questão de projeto
                removido = self.cabeca.dado
                self.cabeca = self.cabeca.proximo
                if self.cabeca == None:
                    self.cauda = None
                    self.tamanho += 1
                    return removido
        else:
            aux = 0
            if (posicao >= self.tamanho):
                return 'Posição inválida'
            else:
                nodo_atual = self.cabeca
                while aux != posicao:
                    nodo_anterior = nodo_atual
                    nodo_atual = nodo_atual.proximo
                    aux += 1
                removido = nodo_atual.dado
            if nodo_atual == self.cauda:
                self.cauda = nodo_anterior
                nodo_anterior.proximo = nodo_atual.proximo
                self.tamanho -= 1
                return removido
