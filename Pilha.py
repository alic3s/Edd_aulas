class Nodo:
    def __init__(self, dado = 0, nodo_anterior = None):
        self.dado = dado
        self.nodo_anterior = nodo_anterior
    
    def __repr__(self):
        return f'{self.dado} -> {self.nodo_anterior}'

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    
    def __repr__(self):
        return '[' + str(self.topo) + ']'
    
    def vazia(self):
        if (self.topo == None):
            return True
        else:
            return False
    
    def insere(self, novo_dado):
        novo_Nodo = Nodo(novo_dado)
        novo_Nodo.anterior = self.topo
        self.topo = novo_Nodo
        self.tamanho += 1

    def remove(self):
        assert self.topo
        self.topo = self.topo.anterior
        self.tamanho -= 1
        removido = self.topo.dado
        self.topo = self.topo.anterior
        return removido


#Exemplo de implementação de pilha
pilha = Pilha()

for i in range(4):
    pilha.insere(i)
    print(f'Insere o valor {i} no topo da pilha: {pilha}')

print(pilha.tamanho)

while pilha.topo != None:
    pilha.remove()
    print('Removendo o elemento que está no topo da pilha: ', pilha)
