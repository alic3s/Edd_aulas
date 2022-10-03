class Nodo:
    def __init__(self, dado = 0, nodo_anterior = None):
        self.dado = dado
        self.nodo_anterior = nodo_anterior
    
    def __repr__(self):
        return '%s --> %s' % (self.dado, self.nodo_anterior)

class Pilha:
    def __init__(self):
        self.topo = None
    
    def __repr(self):
        return '[' + str(self.topo) + ']'
    
    def insere(self, novo_dado):
        novo_Nodo = Nodo(novo_dado)
        novo_Nodo.anterior = self.topo
        self.topo = novo_nodo
        
    def tamanho(self):
        return f'O tamanho da lista é {len(Pilha)}'
    
    def remove(self):
        assert self.topo
        self.topo = self.topo.anterior

pilha = Pilha()

for i in range(4):
    pilha.insere(i)
    print('Insere o valor {0} no topo da pilha: {1}'.format(i,pilha))

print(pilha.tamanho)

while pilha.topo != None:
    pilha.remove()
    print('Removendo o elemento que está no topo da pilha: ', pilha)
