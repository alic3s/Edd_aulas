class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'

class Lista:
    def __init__(self):
        self.cabeca = None
        #self.cauda = None
        #self.tamanho = 0
    
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    
    def vazia(self):
        if (self.cabeca == None):
            return True
        else:
            return False
    
    def insereInicio(lista, novo_dado):
        novo_nodo = Nodo(novo_dado)
        #if self.vazia:
           # self.cabeca = novo_nodo
            #self.cauda = novo_nodo
        #else:
        novo_nodo.proximo = lista.cabeca
        lista.cabeca = novo_nodo
        #self.tamanho += 1
    
    def insereFim(lista, nodo_anterior, novo_dado):
        assert nodo_anterior, "Nodo anterior precisa existir na lista."

        novo_nodo = Nodo(novo_dado)
        #if self.vazia:
            #self.cabeca = novo_nodo
            #self.cauda = novo_nodo
        #else:
        novo_nodo.proximo = nodo_anterior.proximo
        nodo_anterior.proximo = novo_nodo
        #self.tamanho += 1
    
    def remove(self, posicao):
        if self.vazia:
            return f'Impossível remover valor de lista vazia'
        elif (posicao) == 0:    #questão de projeto
                removido = self.cabeca.dado
                self.cabeca = self.cabeca.proximo
                if self.cabeca == None:
                    self.cauda = None
                self.tamanho -= 1
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
    
    def busca(self, dado):
        if self.vazia:
            return 'Elemento não encontrado'
        else:
            nodo_atual = self.cabeca
            for i in range(self.tamanho):
                if nodo_atual.dado != dado:
                    nodo_atual = nodo_atual.proximo
                else:
                    return i
            return 'Elemento não encontrado'
    
    '''def insere(self, novo_dado, posicao):
        if 0 <= posicao <= self.tamanho:
            if posicao == 0:
                self.insereInicio(novo_dado)
                self.tamanho += 1
            elif posicao == (self.tamanho):
                self.insereFim(novo_dado)
                self.tamanho += 1
            else:
                nodo_atual = self.cabeca
                i = 0
                while i != posicao:
                    nodo_anterior = nodo_atual
                    nodo_atual = nodo_atual.proximo
                    i += 1
                removido = nodo_atual.dado
                if nodo_atual == self.cauda:
                    self.cauda = nodo_anterior
                nodo_anterior.proximo = nodo_atual.proximo
                self.tamanho -= 1'''
        

    def inserir(self, novo_dado, posicao):
        posicao = posicao - 1
        if ((posicao < 0) or (posicao > self.tamanho)):
            print ("Posição inválida!")
            return False
        elif (posicao == 0):
            self.inicio = Nodo(novo_dado, None)
        else:
            aux = self.inicio
            for i in range (1, posicao):
                aux = aux.proximo
            aux.proximo = Nodo(novo_dado, aux.proximo)
        self.tamanho = self.tamanho + 1
        return True
