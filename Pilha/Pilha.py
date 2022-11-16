class Nodo:
    def __init__(self, dado = 0, nodo_anterior = None):
        self.dado = dado
        self.anterior = nodo_anterior
    
    def __repr__(self):
        return f'{self.anterior} -> {self.dado}'

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
        if (self.vazia()):
            print('Impossível remover valor de pilha vazia')
        else:
            self.tamanho -= 1
            removido = self.topo.dado
            self.topo = self.topo.anterior
            return removido
    
    def compara(self, pilha2):
        if self.tamanho != pilha2.tamanho:
            return False
        else:
            no_atual1 = self.topo
            no_atual2 = pilha2.topo
            while(no_atual1 != None):
                if(no_atual1.dado != no_atual2.dado):
                    return False
                no_atual1 = no_atual1.anterior
                no_atual2 = no_atual2.anterior
                return True


#Exemplo de implementação de pilha
'''pilha = Pilha()

for i in range(4):
    pilha.insere(i)
    print(f'Insere o valor {i} no topo da pilha: {pilha}')

print(pilha.tamanho)

while pilha.topo != None:
    pilha.remove()
    print('Removendo o elemento que está no topo da pilha: ', pilha)'''


'''pilha = Pilha()
pilha = []
print("Informe os valores da pilha")
print()
# PREENCHENDO A PILHA
for cont in range(7):
    pilha.append(int(input('Informe o valor ' + str(cont + 1) + ' para a pilha: ')))
    print(pilha)

# ESVAZIANDO A PILHA
while len(pilha) > 0:
    pilha.pop()
    print(pilha)

# FINALIZANDO O PROGRAMA
print("Fim...")'''
