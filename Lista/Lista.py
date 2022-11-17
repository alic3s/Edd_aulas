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
            self.tamanho += 1
        else:
            #para compreensão, o dado atual que está na cabeça passa a ser o proximo valor
            #ou seja, como o novo dado inserido vai para a cabeça, ele é o proximo valor
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo
        
    
    def insereFim(self, nodo_anterior, novo_dado):
        assert nodo_anterior, "Nodo anterior precisa existir na lista."

        novo_nodo = Nodo(novo_dado)
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
            self.tamanho += 1
        else:
            self.cauda.proximo = novo_nodo
            self.cauda = novo_nodo
            self.tamanho += 1
    
    
    def remove(self, posicao):
        if self.vazia():
            return f'Impossível remover valor de lista vazia'

        if 0 <= posicao < self.tamanho:
            if posicao == 0:
                removido = self.cabeca.dado
                self.cabeca = self.cabeca.proximo
                self.tamanho -= 1

                if self.cabeca == None:
                    self.cauda = None
                return removido

            else:
                atual = self.cabeca
                aux = 0
                
                while aux != posicao:
                    anterior = atual
                    atual = atual.proximo
                    aux += 1
                removido = atual.dado

                if atual == self.cauda:
                    self.cauda = anterior
                anterior.proximo = atual.proximo
                self.tamanho -= 1
                return removido
        else:
            return 'Posição inválida'
    
    def busca(self, dado):
        if self.vazia():
            return 'Lista vazia'
        else:
            atual = self.cabeca
            posicao = 0

            while atual.dado != dado:
                atual = atual.proximo
                posicao += 1
                
                if posicao == self.tamanho:
                    return 'Não encontrado'
            return posicao 
    
    def inserePosicao(self, novo_dado, posicao):
        novo_nodo = Nodo(novo_dado)
        
        if 0 <= posicao <= self.tamanho:
            if posicao == 0:
                self.insereInicio(novo_dado)
            
            elif posicao == (self.tamanho):
                self.insereFim(novo_dado)
            
            else:
                atual = self.cabeca
                i = 0
                
                while i != posicao:
                    anterior = atual
                    atual = atual.proximo
                    i += 1
                novo_nodo.proximo = atual
                anterior.proximo = novo_nodo
            
                # adaptar a partir daq
                removido = atual.dado
                
                if atual == self.cauda:
                    self.cauda = anterior
                    anterior.proximo = atual.proximo
                    self.tamanho -= 1
    
    def concatenav2(self, lista2):
        self.cauda.proximo = lista2.cabeca
        return self
        
    def concatena(self, lista2):
        listaConc = Lista()
        atual = self.cabeca
        while atual != None:
            listaConc.insereFim(atual.dado)
            atual = atual.proximo
        
        atual = lista2.cabeca

        while atual != None:
            listaConc.insereFim(atual.dado)
            atual = atual.proximo
        return listaConc
